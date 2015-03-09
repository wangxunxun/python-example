#coding=utf-8
'''
Created on 2015年3月9日

@author: xun
'''
import socket
import threading
 
 
inString = ''
outString = ''
nick = ''
 
def DealOut(s):
    global nick, outString
    while True:
        outString = raw_input()
        outString = nick + ': ' + outString
        s.send(outString)
 
def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break
         
 
nick = raw_input("input your nickname: ")
ip = raw_input("input the server's ip adrress: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 8888))
sock.send(nick)
 
thin = threading.Thread(target = DealIn, args = (sock,))
thin.start()
thout = threading.Thread(target = DealOut, args = (sock,))
thout.start()