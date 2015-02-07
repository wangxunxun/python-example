#coding=utf-8
'''
Created on 2015年2月6日

@author: wangxun
'''
#socket server端
#获取socket构造及常量
from socket import *
from thread import *

from SocketServer import TCPServer, BaseRequestHandler  
import SocketServer
import threading
                      
class TestServer():       
    def __init__(self, ip='localhost', iPort=50007):      
          
        self.ip = ip  
        self.iPort = iPort  
        
    def run(self,conn,conns):

        while True:   
            data = conn.recv(1024)
            if not data:
                break       
            for i in conns:
#                if i != conn:
                    i.send(data)
                    
                    
                    
    def start(self):     
        sockobj = socket(AF_INET, SOCK_STREAM)       
        #绑定它至端口号
        sockobj.bind((self.ip, self.iPort))
        #监听，允许5个连结
        sockobj.listen(5)
        conns = []
        while True:
            conn,addr = sockobj.accept()
            addr =addr
            conns.append(conn)


            start_new_thread(self.run, (conn,conns))

if __name__ == "__main__":  
    ts = TestServer()  
    ts.start()  