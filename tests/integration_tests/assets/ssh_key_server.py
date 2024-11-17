#!/usr/bin/env python3
"""
Very simple HTTP daemon server in python for serving ssh keys.
"""
import contextlib
import pathlib
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        ssh_key = self.headers.get("x-ssh-authorized-key")
        self.send_response(200)
        self.wfile.write(bytes(ssh_key))

    def log_message(self, *args, **kwargs):
        pass


server_address = ("", 55555)
httpd = HTTPServer(server_address, Server)
with contextlib.suppress(KeyboardInterrupt):
    httpd.serve_forever()
httpd.server_close()
