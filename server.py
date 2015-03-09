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
import MySQLdb
import string
'''
class TestServer():   
    
    uniquecode = "%uniquecode123%,"      
    createteble = """CREATE TABLE MESSAGE11 (
         ID  INT,
         TOID INT, 
         QUNID INT, 
         NICKNAME  CHAR(20),
         MESSAGE CHAR(40)
         )"""     
         

    def __init__(self, ip='localhost', iPort=50007):      
          
        self.ip = ip  
        self.iPort = iPort  
        
    def savemysql(self):

        self.data1 = self.getdata(self.data)

        conn=MySQLdb.connect(host='69.164.202.55',user='test',passwd='test',db='test',port=3306)
        cur=conn.cursor()
        if cur.execute('show tables like "MESSAGE11"') == 0:
            cur.execute(self.createteble)
#            cur.execute('drop table if exists message')
        try:
#            cur.execute(self.createteble)

            cur.execute("INSERT INTO MESSAGE11(ID, \
       TOID, QUNID, NICKNAME, MESSAGE) \
       VALUES ('%d', '%d', '%d', '%s', '%s' )" % \
       (string.atoi(self.data1['id']), string.atoi(self.data1['toid']), string.atoi(self.data1['qunid']), self.data1['nickname'], self.data1['message']))
            print('save success')
            cur.close()
            conn.commit()
            conn.close()
        except:
            conn.rollback()
        
        
        
    def run(self,conn,conns):

        while True:   

            
            self.data = conn.recv(1024)
            self.savemysql()

            if not self.data:
                break       
            for i in conns:
#                if i != conn:
                    i.send(self.data)

                    
    def getdata(self,data):
        
        newdata={}
        qunid = data[6:data.find(self.uniquecode)]
        newdata['qunid']= qunid
        f = data[data.find(self.uniquecode)+16:]
        id = f[3:f.find(self.uniquecode)]
        newdata['id'] = id
        e = f[f.find(self.uniquecode)+16:]
        toid = e[5:e.find(self.uniquecode)]
        newdata['toid'] = toid
        c= e[e.find(self.uniquecode)+16:]
        nickname=c[9:c.find(self.uniquecode)]
        newdata['nickname']=nickname
        a=c[c.find(self.uniquecode)+16:]        
        sendtime = a[9:a.find(self.uniquecode)]
        newdata['sendtime']=sendtime
        b = a[a.find(self.uniquecode)+16:]
        
        message = b[8:]
        newdata['message']=message
        return newdata
                            
                    
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


#            start_new_thread(self.run, (conn,conns))
            
'''
            

class test(threading.Thread):
    uniquecode = "%uniquecode123%,"      
    createteble = """CREATE TABLE MESSAGE11 (
         ID  INT,
         TOID INT, 
         QUNID INT, 
         NICKNAME  CHAR(20),
         MESSAGE CHAR(40)
         )"""     
         
    def __init__(self, conn, conns):  
        threading.Thread.__init__(self)  
        self.conn = conn
        self.conns = conns
        self.thread_stop = False         
        
        
    def getdata(self,data):
        
        newdata={}
        qunid = data[6:data.find(self.uniquecode)]
        newdata['qunid']= qunid
        f = data[data.find(self.uniquecode)+16:]
        id = f[3:f.find(self.uniquecode)]
        newdata['id'] = id
        e = f[f.find(self.uniquecode)+16:]
        toid = e[5:e.find(self.uniquecode)]
        newdata['toid'] = toid
        c= e[e.find(self.uniquecode)+16:]
        nickname=c[9:c.find(self.uniquecode)]
        newdata['nickname']=nickname
        a=c[c.find(self.uniquecode)+16:]        
        sendtime = a[9:a.find(self.uniquecode)]
        newdata['sendtime']=sendtime
        b = a[a.find(self.uniquecode)+16:]
        
        message = b[8:]
        newdata['message']=message
        return newdata
    def savemysql(self):
        self.data1 = self.getdata(self.data)

        conn=MySQLdb.connect(host='69.164.202.55',user='test',passwd='test',db='test',port=3306)
        cur=conn.cursor()
        if cur.execute('show tables like "MESSAGE11"') == 0:
            cur.execute(self.createteble)
#            cur.execute('drop table if exists message')
        try:
#            cur.execute(self.createteble)

            cur.execute("INSERT INTO MESSAGE11(ID, \
       TOID, QUNID, NICKNAME, MESSAGE) \
       VALUES ('%d', '%d', '%d', '%s', '%s' )" % \
       (string.atoi(self.data1['id']), string.atoi(self.data1['toid']), string.atoi(self.data1['qunid']), self.data1['nickname'], self.data1['message']))
            print('save success')
            cur.close()
            conn.commit()
            conn.close()
        except:
            conn.rollback()      
            
    def run(self):

        while True:   

            try:
                self.data = self.conn.recv(1024)

            
                
                self.savemysql()
    
                if not self.data:
                    break       
                for i in self.conns:
    #                if i != self.conn:
                        i.send(self.data)
            except:
                
                self.conn.close()
                
                
                
                    
                    

    
    def stop(self):  
        self.thread_stop = True    

class jiantingconn(threading.Thread):
    def __init__(self, sockobj):  
        threading.Thread.__init__(self)  
        self.sockobj = sockobj
        self.thread_stop = False    

    def run(self):
        conns= []
        while True:

            conn,addr = self.sockobj.accept()
            addr =addr
            conns.append(conn)
            print conn
            print conns
            test(conn,conns).start()

            
    def stop(self):  
        self.thread_stop = True   

class TestServer11():   
    def __init__(self, ip='localhost', iPort=50007):      
          
        self.ip = ip  
        self.iPort = iPort  
    def start(self):     
        sockobj = socket(AF_INET, SOCK_STREAM)       
        #绑定它至端口号
        sockobj.bind((self.ip, self.iPort))
        #监听，允许5个连结
        sockobj.listen(5)
        return sockobj


                
            
        

if __name__ == "__main__":  
    ts = TestServer11()  
    jiantingconn(ts.start()).start()
    