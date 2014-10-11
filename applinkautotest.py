#coding=utf-8


import os
import unittest

from appium import webdriver
from time import sleep
from _elementtree import Element
import HTMLTestRunner
import datetime

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class APPLINKAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['browserName'] = ''
        desired_caps['device'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2。2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            u'D:/Ford/APPLINK测试工具包/AppLinkTest2.0.apk'
        )
        desired_caps['appPackage'] = 'com.ford.applink'
        desired_caps['appActivity'] = 'com.ford.applink.ui.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        
    def tearDown(self):
        self.driver.quit()

    def cleartext(self,Element):
        s=Element.get_attribute('text') 
        if s:
            Element.clear()
            self.cleartext(Element)    
           
    def ifchecked(self,Element):
        return Element.get_attribute('checked')
    
    def gettext(self,Element):
        return Element.get_attribute('text')
    
    def assertextequal(self,text,ele):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        a=ele.get_attribute('text')
        if a==text:
            print('They are equal.')
        else:
            print('They are not equal.')
       
    def gettextview(self):        
        textview=self.driver.find_elements_by_class_name('android.widget.TextView')
        print('All TextView on the page is ',len(textview))
        i=0
        while i<len(textview):
            print(textview[i].text)
            i=i+1            
            
    def getbutton(self):        
        button=self.driver.find_elements_by_class_name('android.widget.Button')
        print('All Button on the page is ',len(button))
        i=0
        while i<len(button):
            print(button[i].text)
            i=i+1              
    
    def getimageview(self):       
        imageview=self.driver.find_elements_by_class_name('android.widget.ImageView')
        print('All ImageView on the page is ',len(imageview))
        i=0
        while i<len(imageview):
            print(imageview[i].text)
            i=i+1 
    
    def getedittext(self):        
        edittext=self.driver.find_elements_by_class_name('android.widget.EditText')
        print('All EditText on the page is ',len(edittext))
        i=0
        while i<len(edittext):
            print(edittext[i].text)
            i=i+1         
    
    def findelementbyclassnameindex(self,classname,index,name = ''):
        a=self.driver.find_elements_by_class_name(classname)
        b=a[index - 1]
        return b
    

      

class setting(APPLINKAndroidTests):    

    def test_setting(self):
        sleep(2)
        self.findelementbyclassnameindex('android.widget.EditText', 1, 'appname').send_keys('11111111111111111111')
        self.findelementbyclassnameindex('android.widget.EditText', 2, 'vrsynonyms').send_keys('22222')
        self.findelementbyclassnameindex('android.widget.EditText', 3, 'tts text').send_keys('333')
        self.findelementbyclassnameindex('android.widget.CheckBox', 1, 'appname').click()
        self.findelementbyclassnameindex('android.widget.CheckBox', 2, 'media').click()
        self.findelementbyclassnameindex('android.widget.CheckBox', 3, 'language').click()
        self.findelementbyclassnameindex('android.widget.CheckBox', 4, 'Hmi language').click()
#        self.findelementbyclassnameindex('android.widget.Spinner', 1, 'language').click()
        
#        self.findelementbyclassnameindex('android.widget.Spinner', 2, 'hmi language').click()
        self.findelementbyclassnameindex('android.widget.RadioButton', 1, 'wifi').click()
        self.findelementbyclassnameindex('android.widget.RadioButton', 2, 'bluetooth').click()
        self.driver.swipe(100, 600, 100, 200)
        
        



        self.findelementbyclassnameindex('android.widget.Button', 1, 'OK').click()        

        
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(setting)
#    unittest.TextTestRunner(verbosity=2).run(suite)
    
    filename = 'D:/autotestreport/ALE_SERVER_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                               stream=fp,
                               title='ALE server',
                               description='Report_description'
                               )
    runner.run(suite)
