 # -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import traceback



class DFPem:
    def __init__(self, ip=socket.gethostbyname(socket.gethostname()), port=80):
        try:
            self.httpServer = HTTPServer((ip, port), ServerHandler)
        except:
            traceback.print_exc()

    def run(self):

