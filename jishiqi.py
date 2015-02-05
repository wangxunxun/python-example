#coding=utf-8
'''
Created on 2015年2月5日

@author: wangxun
'''
import threading
import httplib2
from urllib import urlencode 
import requests
import time
import json
import xlrd
import xlwt
from xlutils.copy import copy
from __builtin__ import int


class Timer(threading.Thread):         
         def __init__(self, seconds):
             self.runTime = seconds
             threading.Thread.__init__(self)
         def run(self):
             time.sleep(self.runTime)
             print "Buzzzz!! Time's up!"
 
class CountDownTimer(Timer):
         """
         a timer that can counts down the seconds.
         """
         def run(self):
                 counter = self.runTime
                 for sec in range(self.runTime):
                         print counter
                         time.sleep(1.0)
                         counter -= 1
                 print "Done"
 
class CountDownExec(CountDownTimer):

    def __init__(self, seconds, action, args=[]):
        self.args = args
        self.action = action
        CountDownTimer.__init__(self, seconds)
    def run(self):
        CountDownTimer.run(self)
        self.action()
        print self.args

def myAction():
    print "Performing my action with args:"

 
if __name__ == "__main__":         
    t = CountDownExec(3, myAction, ["hello", "world"])
    t.start()