#coding=utf-8
'''
Created on 2014年9月23日

@author: wangxun
'''
import threading 
import time
from time import sleep
import httplib2
from urllib import urlencode 
import requests
import time
import json
import xlrd
import xlwt
from xlutils.copy import copy
from __builtin__ import int



def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim

print "test begin: "+Time()

class timer(threading.Thread):
    def __init__(self,interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.thread_stop=False
    
    def run(self):
        i =1
        while i <= self.interval:
            sleep(1)
            print i
            i=i+1
        print 'stop'

    def stop(self):  
        self.thread_stop = True       

class request(threading.Thread):
    
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.thread_stop=False    
    
    
    
    def run(self):
        try:        
            conn= httplib2.Http(disable_ssl_certificate_validation=True)
            Start=time.time()
            req=conn.request(self.url)
            End=time.time()
            diff= End-Start

            return req[0]['status']
    
        except Exception as err:
            return(err)
    def stop(self):  
        self.thread_stop = True 
 
def test():  

    thread2 = request('http://google.com/')  
    print 1
#    thread1 = timer(10)  
    thread2.start()  
#    thread1.start()  
    t = threading.Timer(5.0, jug)
    t.start() 
  

def sayhello():
        print "hello world"
        global t        #Notice: use global variable!
        t = threading.Timer(5.0, sayhello)
        t.start()

def request1(url):
    try:        
        conn= httplib2.Http(disable_ssl_certificate_validation=True)
        Start=time.time()
        req=conn.request(url)
        End=time.time()
        diff= End-Start

        return req[0]['status']

    except Exception as err:
        return(err)

def jug():
    if request1('http://google.com/'):
        return request1('http://google.com/')[0]['status']


   
if __name__ == '__main__':  
    test()
    print 11
