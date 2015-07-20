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

class appledailyAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['browserName'] = ''
        desired_caps['device'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2。2'
        desired_caps['deviceName'] = 'S5'        
        desired_caps['app'] = PATH(
            u'D:/测试APP/com.nextmedia.apk'
        )                        
        desired_caps['appPackage'] = 'com.nextmedia'
        desired_caps['appActivity'] = 'com.nextmedia.apple.hk.Loading'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 60)        
                
    def tearDown(self):
        self.driver.quit()    

    def gettextviewtext(self):
        textview=self.driver.find_elements_by_class_name('android.widget.TextView')
        i=0
        list = []
        while i<len(textview):         
            list.append(textview[i].text)
            i=i+1 
        return list
        
    def entermainpage(self):
        self.driver.find_element_by_id('com.nextmedia:id/tutorial_show').click()
        self.driver.find_element_by_name(u'略過').click()
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.nextmedia:id/ranking_button')))             


class paihangbang(appledailyAndroidTests):
    def test_zuiguanzhu(self):
        self.entermainpage()
        sleep(1)
        self.assertEqual('1', self.driver.find_element_by_id('com.nextmedia:id/ranking').text)

    def test_zuihit(self):
        self.entermainpage()
        self.driver.find_element_by_name('最Hit').click()
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.nextmedia:id/news_title')))
        self.assertEqual('1', self.driver.find_element_by_id('com.nextmedia:id/ranking').text)

    def test_viewdetail(self):
        self.entermainpage()
        oldtitle = self.driver.find_element_by_id('com.nextmedia:id/news_title').text
        self.driver.find_element_by_id('com.nextmedia:id/news_title').click()
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.nextmedia:id/news_fbComments')))
        self.assertEqual(oldtitle, self.driver.find_element_by_id('com.nextmedia:id/news_title').text)

    def test_checkitems(self):
        self.entermainpage()
        i =0
        while i<8:
            self.driver.swipe(100, 1580, 100, 560, 2000)
            i=i+1
        self.assertIn('20', self.gettextviewtext())    

class pingguofb(appledailyAndroidTests):
    def test_enterpingguofb(self):
        self.entermainpage()
        sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.nextmedia:id/header_menu')))
        sleep(1)
        self.driver.find_element_by_id('com.nextmedia:id/header_menu').click()
        self.wait.until(EC.text_to_be_present_in_element((By.NAME,u'蘋果FB'),u'蘋果FB'))
        self.driver.find_element_by_name(u'蘋果FB').click()
        sleep(30) 
        self.assertTrue(self.driver.find_element_by_class_name('android.view.View'))
        
           
        
if __name__ == '__main__':
    suite_paihangbang = unittest.TestLoader().loadTestsFromTestCase(paihangbang)
    suite_pingguofb = unittest.TestLoader().loadTestsFromTestCase(pingguofb)
    alltests =  unittest.TestSuite([suite_paihangbang,suite_pingguofb])

#    test = unittest.TestLoader().loadTestsFromName('appledaily.pingguofb.test_enterpingguofb')
#    unittest.TextTestRunner(verbosity=2).run(test)
    
    filename = 'D:/autotestreport/appledaily_android_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                               stream=fp,
                               title=u'苹果动新闻自动化测试报告',
                               description=u'本报告为demo版，主要测试排行榜和苹果FB两个模块'
                               )
    runner.run(alltests)
