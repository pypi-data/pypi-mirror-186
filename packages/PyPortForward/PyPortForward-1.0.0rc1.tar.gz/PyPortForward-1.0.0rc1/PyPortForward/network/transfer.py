from threading import Thread
from gc import collect
import socket
import logging

import PyPortForward as ppf

"""
PROXY
{
    "origin": {
        "UUID": { # Connection_id
            "server": "UUID", # Server_id
            "clients": {
                "UUID1": socket.socket(),
                "UUID2": socket.socket()
            },
        }
    },
    "server": {
        "UUID": { # Server_id
            "name": "onTDB's Server 01",
            "socket": socket.socket(),
            "token": "UUID",
        }
    }
}

SERVER
{
    "origin": {
        "UUID": {
            "ip": "0.0.0.0",
            "port": 1234,
            "clients": {
                "UUID1": socket.socket(),
                "UUID2": socket.socket()
            },
            "clientthreads": {
                "UUID1": Thread(),
                "UUID2": Thread()
            }
        }
    },
    "proxy": {
        "name": "onTDB's Proxy 01",
        "socket": socket.socket(),
        "token": "128BIT",
        "thread": Thread()
    }
}
"""
# connections => ppf.connections

def handle_proxy(buffer, direction, src, client_id, server_name, connection_id): #direction: true ==> goto origin server
    '''
    intercept the data flows between local port and the target port
    '''
    src_ip, src_port = src.getsockname()
    if direction:#ppf.connections[connection_id]["server"]["name"]
        info, buffer = ppf.network.attach_info(client_id, connection_id, buffer)
        logging.info(f"{src_ip}:{src_port} ({client_id}) -> {server_name} ({connection_id}) :: {len(buffer)} bytes")
    else:
        info, buffer = ppf.network.parse_info(buffer)
        connection_id = info["conn_id"]
        client_id = info["client_id"]
        src_ip, src_port = ppf.connections["origin"][connection_id]["clients"][client_id].getsockname()
        logging.info(f"{src_ip}:{src_port} ({client_id}) <- {server_name} ({connection_id}) :: {len(buffer)} bytes")
    return info, buffer

def handle_server(buffer, direction, client_id, origin, connection_id, proxy_name):
    '''
    intercept the data flows between local port and the target port
    '''
    origin_ip, origin_port = origin.getsockname()
    if direction:
        info, buffer = ppf.network.parse_info(buffer)
        connection_id = info["conn_id"]
        client_id = info["client_id"]
        origin_ip, origin_port = ppf.connections["origin"][connection_id]["socket"].getsockname()
        logging.debug(f"{proxy_name} ({client_id}) -> {origin_ip}:{origin_port} ({connection_id}) :: {len(buffer)} bytes")
    else:
        info, buffer = ppf.network.attach_info(client_id, connection_id, buffer)
        logging.debug(f"{proxy_name} ({client_id}) <- {origin_ip}:{origin_port} ({connection_id}) :: {len(buffer)} bytes")        
    return info, buffer

def transfer_info(src, dst, client_id, server_name, connection_id, direction):
    '''
    Pass with information to the destination
    '''
    src_ip, src_port = src.getsockname()
    dst_ip, dst_port = dst.getsockname()
    while True:
        try:
            buffer = src.recv(4096)
            if len(buffer) > 0:
                if direction: # Proxy -> Server
                    info, buffer = handle_proxy(buffer, direction, src, client_id, server_name, connection_id)
                else: # Server -> Proxy
                    info, buffer = handle_server(buffer, direction, client_id, src, connection_id, server_name)
                dst.send(buffer)
        except Exception as e:
            logging.error(repr(e))
            if direction and dst.fileno() == -1:
                logging.critical(msg="Origin socket is closed!")
                break
            elif not direction and src.fileno() == -1:
                logging.critical(msg="Proxy socket is closed!")
                break
            break
    if direction:
        for sock in ppf.connections["origin"][connection_id]["clients"].values():
            sock.close()
    else:
        for sock in ppf.connections["origin"].values():
            sock.close()

def transfer_raw(src, src_name, direction):
    src_ip, src_port = src.getsockname()
    while True:
        try:
            buffer = src.recv(4096)
            if len(buffer) > 0:
                if direction: # Server -> Origin
                    info, buffer = handle_server(buffer, direction, None, src, None, src_name)
                else: # Proxy -> client
                    info, buffer = handle_proxy(buffer, direction, src, None, src_name, None)

                if info["mode"] == "OPEN" and direction:
                    newconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    newconn.connect((ppf.connections["origin"][info["conn_id"]]["ip"], ppf.connections["origin"][info["conn_id"]]["port"]))
                    ppf.connections["origin"][info["conn_id"]]["clients"][info["client_id"]] = newconn
                    logging.info(f"[ESTABLISHING] {src_name} {info['client_id']} -> {ppf.connections['origin'][info['conn_id']]['ip']}:{ppf.connections['origin'][info['conn_id']]['port']} ({info['conn_id']})")

                    newthr = Thread(target=transfer_info, args=(newconn, src, info["client_id"], src_name, info["conn_id"], False))
                    newthr.daeomon = True
                    newthr.start()
                    ppf.connections["origin"][info["conn_id"]]["clientthreads"][info["client_id"]] = newthr
                    continue
                elif info["mode"] == "CLOSE":
                    logging.warning(f"Closing connect {src_ip}:{src_port}! (Client Request)")
                    ppf.connections["origin"][info["conn_id"]]["clients"][info["client_id"]].close()
                    del(ppf.connections["origin"][info["conn_id"]]["clients"][info["client_id"]])
                    del(ppf.connections["origin"][info["conn_id"]]["clientthreads"][info["client_id"]])
                    collect()
                    continue
                elif info["mode"] == "DATA":
                    if direction:
                        ppf.connections["origin"][info["conn_id"]]["clients"][info["client_id"]].send(buffer)
                    else:
                        ppf.connections["origin"][info["conn_id"]]["server"]["socket"].send(buffer)
                else:
                    logging.error(f"Unknown mode {info['mode']} from {info['client_id']}!")
        except Exception as e:
            logging.error(repr(e))
            # Check socket are closed
            if src.fileno() == -1:
                logging.critical(msg="Proxy socket is closed!")
                break
            break
