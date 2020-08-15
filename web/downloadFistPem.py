 # -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import sys
import time
import traceback

class DFPem:
    @staticmethod
    def run(ip="0.0.0.0", port=80):
        filename = 'test/test.txt'
        try:
            class ServerHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.send_header("Content-type", "text/plain; charset=utf-8")
                    self.end_headers()
                    with open(filename, 'rb') as f:
                        self.wfile.write(f.read())
                    os.remove(filename)

            httpServer = HTTPServer((ip, port), ServerHandler)
            httpServer.serve_forever()
        except FileNotFoundError:
            sys.exit(1)
        except:
            traceback.print_exc()
