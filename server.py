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
'''
#''代表服务器为localhost
myHost = '10.27.0.189'
#在一个非保留端口号上进行监听
myPort = 50007

#设置一个TCP socket对象
sockobj = socket(AF_INET, SOCK_STREAM)
#绑定它至端口号
sockobj.bind((myHost, myPort))
#监听，允许5个连结
sockobj.listen(5)

'''
'''
#直到进程结束时才结束循环
while True:
    #等待下一个客户端连结
    connection, address = sockobj.accept( )

    #连结是一个新的socket
    print 'Server connected by', address
    while True:
        #读取客户端套接字的下一行
        data = connection.recv(1024)
        #如果没有数量的话，那么跳出循环
        if not data: break
        #发送一个回复至客户端
        connection.send('Echo=>' + data)
    #当socket关闭时eof
    connection.close( )
'''        
'''        
def clientthread(conn,conns):
    
    while True:

        data = conn.recv(1024)
        if not data:
            break
        for i in conns:
            if i != conn:
                print i
                print data
                i.send(data)
    conn.close()

conns = []
while True:
    conn,addr=sockobj.accept()
    conns.append(conn)
    
    print conns

    start_new_thread(clientthread, (conn,conns,))


'''
class connectclient(threading.Thread):
    def __init__(self,conn):
        self.conn = conn
    
    def collectconn(self):
        conns = []
        while True:

            conns.append(self.conn)
            print conns
            return conns
        
        
    def run(self):

        while True:   
            data = self.conn.recv(1024)
            if not data:
                break       
            for i in self.collectconn():
                if i != self.conn:
                    i.send(data)
                
        
        
           
    
    
class TestServer():      
    def __init__(self, ip='10.27.0.189', iPort=50007):      
          
        self.ip = ip  
        self.iPort = iPort  
    def start(self):     
        sockobj = socket(AF_INET, SOCK_STREAM)       
        #绑定它至端口号
        sockobj.bind((self.ip, self.iPort))
        #监听，允许5个连结
        sockobj.listen(5)
        while True:
            conn,addr = sockobj.accept()
            t= connectclient(conn)
            start_new_thread(t.run, ())

if __name__ == "__main__":  
    ts = TestServer()  
    ts.start()  