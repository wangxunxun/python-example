#coding=utf-8
'''
Created on 2015年2月4日

@author: wangxun
'''
import httplib2
from urllib import urlencode 
import requests
import time
import json
import xlrd
import xlwt
from xlutils.copy import copy
from __builtin__ import int
'''

def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim

print Time()

h=httplib2.Http()

feedbackinfo = {
                    "name": "wangxun",
                    "email": "59853844@qq.com",
                    "telephone": '11111111111',
                    "im": '454545',
                    "feedback": '454545',
                    "filename": '454545',
                    "version":   '45345',
                    "environment": 'darwin'
                }


#response = requests.post('http://ale.link-pub.cn/feedbacks', feedbackinfo)
#print response




#resp, content = h.request('http://ale.link-pub.cn/feedbacks' ,"POST", urlencode(feedbackinfo))
#print 'response=', resp
#print "content=" ,content
'''

def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim

print "test begin: "+Time()
#开始时间

oldwb=xlrd.open_workbook(r'C:/Users/wangxun/Documents/url.xlsx')
oldsh = oldwb.sheet_by_index(0)
nrows=oldsh.nrows
newwb=copy(oldwb)
newsh=newwb.get_sheet(0)
#第一次调用xlrd，xlwt

def GetHttpStatus(url):
    try:        
        conn= httplib2.Http(disable_ssl_certificate_validation=True)
        req=conn.request(url)
        
        return req[0]['status']

    except Exception as err:
        return(err)
#https请求方法

def GetHttpTime(url):
    conn= httplib2.Http(disable_ssl_certificate_validation=True)
    Start=time.time()
    req=conn.request(url)
    End=time.time()
    diff= End-Start
    return diff
#获取请求时间

for i in range(1,nrows):
    url1=oldsh.cell_value(i,1)    
    url=url1
    newsh.write(i,2,GetHttpStatus(url))
    newsh.write(i,5,Time())
    newsh.write(i,6,GetHttpTime(url))
    if GetHttpTime(url) < 1.0:
        newsh.write(i,7,'Normal')
    else:
        newsh.write(i,7,'Timeout')
newwb.save('C:/Users/wangxun/Documents/newurl.xls')
#将复制过的数据保存在newurl.xls

newwb=xlrd.open_workbook(r'C:/Users/wangxun/Documents/newurl.xls')
newsh=newwb.sheet_by_index(0)
nroNws=newsh.nrows
oldwb1=copy(newwb)
oldsh1=oldwb1.get_sheet(0)
#第二次调用xlrd，xlwt，复制newurl.xls到url.xls进行实际结果与预期结果对比

for n in range(1,nroNws):
    AC_reusult=newsh.cell(n,2).value + '.0'
    EX_reusult=newsh.cell(n,3).value
    EX_reusult=str(EX_reusult)
    if EX_reusult == AC_reusult:
        oldsh1.write(n,4,"PASS")
    else:
        oldsh1.write(n,4,"FAIL")
oldwb1.save('C:/Users/wangxun/Documents/url.xls')

if 200==200:
    print 'aaaa'

print "test over: "+Time()
#结束时间


'''

#-*- coding: utf-8 -*-
import httplib2,time

relist=[]
fname=raw_input('请输入url： ')
f1=open(fname,'r')
relist=f1.readlines()
print relist
f1.close
print len(relist)
count=len(relist)

def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim

def GetHttpStatus(url):
    try:
        conn= httplib2.Http(disable_ssl_certificate_validation=True)
        req=conn.request(url)
        return req[0]['status']    
    except Exception as err:
        return(err)

for m in range(0,count):
    url1=relist[m]
    url=url1.strip()
    print url
    if GetHttpStatus(url) !="200":
        f2=open("urlhttps-result.txt","a")
        f2.write("测试日期："+Time()+"\n")
        f2.write( "请求失败，错误代码为："+GetHttpStatus(url))
        f2.write("\n")
        f2.close()
        print "请求失败"
    else:
        print GetHttpStatus(url), "请求成功------------------------"
'''