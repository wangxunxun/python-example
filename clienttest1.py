#coding=utf-8
'''
Created on 2015年3月9日

@author: xun
'''
import socket
import threading
import json
from time import ctime
from setuptools.command import install_scripts
 
inString = ''
outString = ''
nick = ''
 
def DealOut(s):
    global nick, outString
    while True:
        outString = raw_input()
        outString={"qunid":qunid,"send":username,"receive":touser,"nickname":nick,"message":outString,'time':ctime()}
        outString= json.dumps(outString)
#        outString = nick + ': ' + outString
        s.send(outString)
 
def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)            
            if not inString:
                break
            if inString[0]=='{':
                inString = json.loads(inString)    
                if inString['qunid']=='0':
                    if inString['send']==username:
                        print 'send:'+str(inString)                
                    if inString['receive'] == username:
                        print 'receive:'+str(inString)   
                elif inString['qunid'] == qunid:
                    if inString['send']==username:
                        print 'qunsend:'+str(inString)    
                    else:
                        print "qunreceive:"+str(inString)
            else:
                print inString 
        except:
            break
         
qunid =  raw_input("input your qunid: ")
nick = raw_input("input your nickname: ")
ip = raw_input("input the server's ip adrress: ")
username = raw_input("input the server's username: ")
touser = raw_input("input the server's touser: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 8888))
sock.send(nick)
 
thin = threading.Thread(target = DealIn, args = (sock,))
thin.start()
thout = threading.Thread(target = DealOut, args = (sock,))
thout.start()