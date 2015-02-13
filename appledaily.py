#coding=utf-8


import os
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from time import sleep
from _elementtree import Element
import HTMLTestRunner
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class BotaiAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['browserName'] = ''
        desired_caps['device'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2。2'
#        desired_caps['deviceName'] = 'Android Emulator'

        desired_caps['deviceName'] = 'ZTEU930HD'        
        desired_caps['app'] = PATH(
            u'/Users/wangxun/Documents/test app/iVokaMINIX_1.6.0.apk'
        )
                
        
        desired_caps['appPackage'] = 'com.pateo.mobile'
        desired_caps['appActivity'] = 'com.pateo.mobile.ui.account.LoginActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 10)        


        
    def tearDown(self):
        self.driver.quit()unner