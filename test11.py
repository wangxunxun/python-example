#coding=utf-8
'''
Created on 2014年9月23日

@author: wangxun
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import string
from time import sleep

class Test11(unittest.TestCase):
    def setUp(self):
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('C:\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://42.96.155.222:8888/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def tablelasttr(self,css):
        a = str(css)
        b = a.find('tr:')
        c = a.find('(',b,-1)
        d = a.find(')',b,-1)        
        e = a[c+1:d]      
        f = string.atoi(e)        
        while f>1:
            g = a[:c+1] +str(f) + a[d:]
            f -=1
            try:
                return self.driver.find_element_by_css_selector(g)
                break
            except:
                continue

             

        
        
        
    
    def test_11(self):
        driver = self.driver
        driver.get(self.base_url + "login?next=%2F")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        sleep(5)
        driver.find_element_by_css_selector('#li_id_user').click()
        sleep(10)
        self.tablelasttr('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(11) > td:nth-child(7) > button').click()
        sleep(5)
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    

    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()