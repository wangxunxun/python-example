#coding=utf-8
'''
Created on 2015年2月6日

@author: wangxun
'''
import sys
from socket import *
from thread import *
import time
def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim



class client:

    uniquecode = "%uniquecode123%,"    
    
    def __init__(self,ip = 'localhost',iPort = 50007):
        self.ip = ip  
        self.iPort = iPort  

    def create(self):
        sockobj = socket(AF_INET, SOCK_STREAM)

        sockobj.connect((self.ip, self.iPort))
        start_new_thread(self.receive, (sockobj,))
           
        self.send(sockobj)
        
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
        
        
        
        
    def receive(self,sockobj):
        while True:
            data = sockobj.recv(1024)
            data = self.getdata(data)
            if not data:
                break
            if self.qunid=='0':
                if data['id']==self.id:
                    print 'send:'+str(data)                
                if data['toid'] == self.id:
                    print 'receive:'+str(data)   
            elif data['qunid'] == self.qunid:
                if data['id']==self.id:
                    print 'qunsend:'+str(data)    
                else:
                    print "qunreceive:"+str(data)

                

    def send(self,sockobj):

        self.qunid = raw_input('qunid:')
        if not self.qunid:
            self.qunid ='0'
        self.id = raw_input('id:')      
        if not self.id:
            self.id = '0'  
        self.toid = raw_input('toid:') 
        if not self.toid:
            self.toid ='1'
        self.nickname = raw_input("input your name: ")
        if not self.nickname:
            self.nickname = 'troywang'


        while True:
            message = raw_input("input message: ")        
            sockobj.send('qunid:'+self.qunid+self.uniquecode+'id:'+self.id+self.uniquecode+'toid:'+self.toid+self.uniquecode+'nickname:'+self.nickname +self.uniquecode+ 'sendtime:'+Time()+self.uniquecode+'message:'+ message)





if __name__ == "__main__":  
    cl = client()
    cl.create()



