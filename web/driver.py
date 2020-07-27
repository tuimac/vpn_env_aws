#!/usr/bin/env python3

from downloadFistPem import DFPem
from threading import Thread
import urllib.request
import socket
import time

def getRequest(url):
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.read())

def test():
    dfp = DFPem()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 80
    url = 'http://' + ip + ':' + str(port)

    dfp = Thread(target=test)
    dfp.daemon = True
    dfp.start()
    time.sleep(1)
    getRequest(url)
