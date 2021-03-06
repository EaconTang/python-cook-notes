# -*- coding: utf-8 -*-
import argparse
import datetime

import xmlrpc

import Meter

PATH = "/meter"


class RequestHandler(xmlrpc.server.SimpleXMLRPCRequestHandler):
    rpc_path = (PATH,)


def main():
    host, port, notify = handle_commandline()
    manager, server = setup(host, port)
    print("Meter server startup at {} on {}:{}{}".format(
        datetime.datetime.now().isoformat()[:19], host, port, PATH
    ))
    try:
        if notify:
            with open(notify, "wb") as file:
                file.write(b"\n")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\rMeter server shutdown ad {}".format(
            datetime.datetime.now().isoformat()[:19]
        ))
        manager._dump()


HOST = "localhost"
PORT = 11002


def handle_commandline():
    parser = argparse.ArgumentParser(conflict_handler="resolve")
    parser.add_argument("-h", "--host", default=HOST,
                        help="hostname [default %(default)s]")
    parser.add_argument("-p", "--port", default=PORT, type=int,
                        help="port number [default %(default)d]")
    parser.add_argument("--notify", help="specify a notification file")
    args = parser.parse_args()
    return args.host, args.port, args.notify


def setup(host, port):
    manager = Meter.Manager()
    server = xmlrpc.server.SimpleXMLRPCServer((host, port),
                                              requestHandler=RequestHandler,
                                              logRequests=False)
    server.register_introspection_functions()
    for method in (manager.login, manager.get_job, manager.submit_reading, manager.get_status):
        server.register_function(method)
    return manager, server
