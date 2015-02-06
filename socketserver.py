#coding=utf-8
'''
Created on 2015年2月6日

@author: wangxun
'''
import SocketServer
from SocketServer import (TCPServer,StreamRequestHandler  as SRH,
    ThreadingTCPServer)
from time import ctime
from pip._vendor.requests.api import request

class MyRequestHandler(SRH):
    def handle(self):
        while True:

            data = self.request.recv(1024)
            

            print "receive from(%r):%r " % (self.client_address,data)
            data1 =ctime() +':'+data
            print data1
            self.request.sendall(data1)

tcpSer=ThreadingTCPServer(("10.27.0.189",50007),MyRequestHandler)
while True:
    print '44'
    
    print tcpSer.get_request()[0]
    print "waiting for connection"
    tcpSer.serve_forever()
