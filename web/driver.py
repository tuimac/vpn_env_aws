#!/usr/bin/env python3

from downloadFistPem import DFPem
from threading import Thread
import urllib.request
import traceback
import socket
import time

def getRequest(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.read())

def test():
    try:
        filepath = 'test/test.txt'
        with open(filepath, 'a') as f:
            f.write('tesssst')
        DFPem.run()
        print('done')
    except Error as e:
        raise e

if __name__ == '__main__':
    try:
        ip = socket.gethostbyname(socket.gethostname())
        port = 80
        url = 'http://' + ip + ':' + str(port)

        dfp = Thread(target=test)
        dfp.daemon = True
        dfp.start()
        time.sleep(1)
        for i in range(5):
            getRequest(url)
            time.sleep(1)
    except:
        pass
