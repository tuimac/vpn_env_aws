 # -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import traceback

class DFPem:

    @staticmethod
    def run(ip="0.0.0.0", port=80):
        try:
            class ServerHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    param = urlparse(self.path)
                    query = parse_qs(param.query)
                    print(param)
                    print(query)

            self.httpServer = HTTPServer((ip, port), ServerHandler)
            self.httpServer.serve_forever()
        except:
            traceback.print_exc()
