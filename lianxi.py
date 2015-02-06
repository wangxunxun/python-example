#coding=utf-8
'''
Created on 2015年2月6日

@author: wangxun
'''
import httplib2

def GetHttpStatus(url):
    try:        
        conn= httplib2.Http(disable_ssl_certificate_validation=True)
        req=conn.request(url)
        
        return req[0]['status']
        conn.request

    except Exception as err:
        return(err)
#https请求方法


print GetHttpStatus('http://www.google.com')