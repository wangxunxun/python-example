#coding=utf-8
'''
Created on 2015年2月6日

@author: wangxun
'''
import sys
from socket import *
from thread import *

serverHost = '10.27.0.189'
serverPort = 50007

#发送至服务端的默认文本

#如果参数大于1的话，连结的服务端为第一个参数


#建立一个tcp/ip套接字对象
sockobj = socket(AF_INET, SOCK_STREAM)
#连结至服务器及端口
sockobj.connect((serverHost, serverPort))

def receive(sockobj):
    while True:
        data = sockobj.recv(1024)
        if not data:
            break
        
        print "receive:" + repr(data)

def send(sockobj):
    while True:
        message = raw_input("raw_input: ")        
        sockobj.send(message)



start_new_thread(receive, (sockobj,))
   
send(sockobj)

    



