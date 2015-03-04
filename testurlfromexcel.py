#coding=utf-8
'''
Created on 2015年2月4日

@author: wangxun
'''
import httplib2
from urllib import urlencode 
import requests
import time
import json111
import xlrd
import xlwt
from xlutils.copy import copy
from __builtin__ import int


def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim

class testurlfromexcel:
    def __init__(self,old,new,old1):
        self.old=old
        self.new=new
        self.old1=old1

    def run(self):
        self.savenewwb()
        self.compareresult()
    
    
    
    def savenewwb(self):
        oldwb=xlrd.open_workbook(self.old)
        oldsh = oldwb.sheet_by_index(0)
        nrows=oldsh.nrows
        newwb=copy(oldwb)
        newsh=newwb.get_sheet(0)    
        for i in range(1,nrows):
            url1=oldsh.cell_value(i,1)    
            url=url1
            newsh.write(i,3,self.GetHttpStatus(url))
            newsh.write(i,5,Time())
            newsh.write(i,6,self.GetHttpTime(url))
            if self.GetHttpTime(url) < 1.0:
                newsh.write(i,7,'Normal')
            else:
                newsh.write(i,7,'Timeout')    
        newwb.save(self.new)
    
    def compareresult(self):    
        newwb=xlrd.open_workbook(self.new)
        newsh=newwb.sheet_by_index(0)
        nroNws=newsh.nrows
        oldwb1=copy(newwb)
        oldsh1=oldwb1.get_sheet(0)            
        for n in range(1,nroNws):
            AC_reusult=newsh.cell(n,3).value + '.0'           
            EX_reusult=newsh.cell(n,2).value
            EX_reusult=str(EX_reusult)
            if EX_reusult == AC_reusult:
                oldsh1.write(n,4,"PASS")
            else:
                oldsh1.write(n,4,"FAIL")
        oldwb1.save(self.old1)
    
    def GetHttpStatus(self,url):
        try:        
            res= requests.get(url,timeout=1)
            
            return str(res.status_code)
    
        except:
            return "504"
    
    def GetHttpTime(self,url):    
        try:
            Start=time.time()    
            requests.get(url,timeout=1)
            End=time.time()
            diff= End-Start
            return diff
        except:
            End=time.time()
            diff= End-Start
            return diff

if __name__ == "__main__":  
    print "test begin: "+Time()
    old = 'C:/Users/wangxun/Documents/url.xlsx'    
    new = 'C:/Users/wangxun/Documents/newurl.xls'
    old1 = 'C:/Users/wangxun/Documents/url.xls'
    test = testurlfromexcel(old,new,old1)
    test.run()
    print "test over: "+Time()


