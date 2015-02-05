#coding=utf-8
'''
Created on 2014年10月30日

@author: wangxun
'''
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from selenium.webdriver.common.by import By
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = "com.beyondsoft.app1"
#        app = os.path.join(os.path.dirname(__file__),
#                           u'/Users/wangxun/Documents/test app/Payload',
#                           'AppLinkTester2.app')
#        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '7.1',
                'deviceName': 'iPhone Simulator',
                'udid':'941da79cada57dd70a1a8a2740063914f3e758ea'
            })

        self.wait = WebDriverWait(self.driver, 10)      
    def tearDown(self):
        self.driver.quit()




    def test_changyongdizhi(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME,u'home nav left'))) 
        self.driver.find_element_by_name('home nav left').click()
        i=100
        while i>=1:

            self.driver.find_element_by_name(u'常用地址').click()
            print self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text
            self.assertEqual(u'我的地址薄', self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text)
#            self.driver.find_element_by_name(u'返回').click()
            self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()
            i=i-1
            
    def test_gerenxinxi(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME,u'home nav left')))
        self.driver.find_element_by_name('home nav left').click()        
        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]').click()
        checktext = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[3]/UIATextField[1]').text
        print checktext
        self.assertIn('4000889900', checktext)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)