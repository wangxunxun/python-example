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
        self.driver.quit()

    def login(self,username,password):
        sleep(3)
        self.username = username
        self.password = password  
        self.findelementbyclassnameindex('android.widget.EditText', 1, 'username').send_keys(self.username)
        self.findelementbyclassnameindex('android.widget.EditText', 2, 'password').send_keys(self.password)
        self.findelementbyclassnameindex('android.widget.Button', 1, 'login').click()


    def entersettingpage(self):
        self.login('13659874858', '123456')
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/mainpage_date_top')))        
        self.driver.find_element_by_id('com.pateo.mobile:id/mainpage_thr_img').click()
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/iv_icon')))
        self.findelementbyclassnameindex('android.widget.LinearLayout', 16, 'systemsetting').click()
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/lin_setting_user_info')))
        
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
    
    def gettextviewtext(self):
        textview=self.driver.find_elements_by_class_name('android.widget.TextView')
        i=0
        list = []
        while i<len(textview):         
            list.append(textview[i].text)
            i=i+1 
        return list
            
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
    
    def getsecondtext(self,ele):
        self.element = ele
        self.a = self.element.text
        return self.a.split('.')[1]
        
      

class login(BotaiAndroidTests):    
    u'''登陆测试用例集'''
    def test_login(self):
        u'''登陆成功'''
        self.login('13659874858', '123456')
#        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'android.widget.Toast')))


#        print self.driver.find_element_by_class_name('android.widget.Toast').text
        
        
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/mainpage_date_top')))

        self.assertIn(u'今天', self.gettextviewtext())
        
class setting(BotaiAndroidTests):       
    u'''设置测试用例集'''

    
    def feedback(self,value):
        self.feedbackvalue = value           
        self.driver.find_element_by_id('com.pateo.mobile:id/edit_text').clear()
        self.driver.find_element_by_id('com.pateo.mobile:id/edit_text').send_keys(self.feedbackvalue)
        self.driver.find_element_by_id('com.pateo.mobile:id/choose_pic_button').click()            
        self.driver.find_element_by_id('com.pateo.mobile:id/btn_setting_user_take_picture').click()
        sleep(1)
        self.driver.tap([(536,1786)], 1000)    
        sleep(2)
        self.driver.find_element_by_id('com.sec.android.app.camera:id/save').click()  
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/send_button')))
        self.driver.find_element_by_id('com.pateo.mobile:id/send_button').click()
        
    def personalinformation(self,nickname,contact,telephone,drivernumber):
        self.nickname = nickname
        self.contact = contact
        self.telephone = telephone
        self.drivernumber = drivernumber
        if self.nickname:
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_nickname').click()
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_nickname').send_keys(self.nickname)
            self.driver.hide_keyboard()
        if self.contact:
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact').click()
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact').send_keys(self.contact)
            self.driver.hide_keyboard()
        if self.telephone:
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact_phone').click()
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact_phone').send_keys(self.telephone)
            self.driver.hide_keyboard()
        if self.drivernumber:
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_driver_num').click()
            self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_driver_num').send_keys(self.drivernumber)
            self.driver.hide_keyboard()
                       
    def test_feedback(self):
        u'''发送反馈测试用例'''
        self.value = '22222'
        self.entersettingpage()     
        self.driver.find_element_by_id('com.pateo.mobile:id/lin_setting_feedback').click()      
        self.feedback(self.value)
        sleep(10)
        self.assertIn(self.value, self.findelementbyclassnameindex('android.widget.TextView', 3, 'feedbackvalue').text)
        
    def test_personalinformation(self):
        u'''更新个人信息测试用例'''
        self.entersettingpage()   
        self.driver.find_element_by_id('com.pateo.mobile:id/lin_setting_user_info').click()
        self.nickname = '111'
        self.contact = '1'
        self.telephone = None
        self.drivernumber = None
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=-1)
        a = now + delta
        self.date = a.strftime('%Y-%m-%d')


        
        if self.nickname:
            self.nickmame1 = self.getsecondtext(self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_nickname')) + self.nickname

        if self.contact:
            self.contact1 = self.getsecondtext(self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact')) + self.contact

        if self.telephone:
            self.telephone1 = self.getsecondtext(self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact_phone')) + self.telephone
        if self.drivernumber:
            self.drivernumber1 = self.getsecondtext(self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_driver_num')) + self.drivernumber        
        self.personalinformation(self.nickname, self.contact, self.telephone, self.drivernumber)
        
        self.driver.find_element_by_id('com.pateo.mobile:id/tv_setting_user_effective').click()
        self.findelementbyclassnameindex('android.widget.ImageButton', 6, 'day').click()        
        self.driver.find_element_by_id('android:id/button1').click()        
        self.driver.find_element_by_id('com.pateo.mobile:id/tv_setting_user_effective_year').click()
        self.driver.find_element_by_id('com.pateo.mobile:id/tv_year_option_3').click()
       
        self.driver.find_element_by_id('com.pateo.mobile:id/iv_setting_user_head_pic').click()   
          
        self.driver.find_element_by_id('com.pateo.mobile:id/btn_setting_user_take_picture').click()
        sleep(4)

        self.driver.tap([(536,1786)], 1000)    
        
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.sec.android.app.camera:id/save')))
        self.driver.find_element_by_id('com.sec.android.app.camera:id/save').click()   
      
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/activity_frame_title_btn_right')))
        self.driver.find_element_by_id('com.pateo.mobile:id/activity_frame_title_btn_right').click()
        sleep(10)
        self.wait.until(EC.element_to_be_clickable((By.ID,'com.pateo.mobile:id/et_setting_user_nickname')))
        self.driver.find_element_by_id('com.pateo.mobile:id/activity_frame_title_btn_left').click()
        self.driver.find_element_by_id('com.pateo.mobile:id/lin_setting_user_info').click()      
        sleep(1)
        


        
#        self.assertIn(self.nickmame1, self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_nickname').text)
#        self.assertIn(self.contact1, self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact').text)
#        self.assertIn(self.telephone1, self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_emergency_contact_phone').text)
#        self.assertIn(self.drivernumber1, self.driver.find_element_by_id('com.pateo.mobile:id/et_setting_user_driver_num').text)         
        self.assertIn(u'长期', self.driver.find_element_by_id('com.pateo.mobile:id/tv_setting_user_effective_year').text)
        self.assertIn(self.date, self.driver.find_element_by_id('com.pateo.mobile:id/tv_setting_user_effective').text)        

if __name__ == '__main__':
    suite_login = unittest.TestLoader().loadTestsFromTestCase(login)
    suite_setting = unittest.TestLoader().loadTestsFromTestCase(setting)
    alltests =  unittest.TestSuite([suite_login,suite_setting])
    test = unittest.TestLoader().loadTestsFromName('botaiautotest.setting.test_feedback')
    unittest.TextTestRunner(verbosity=2).run(test)
'''   
    filename = 'D:/autotestreport/ALE_SERVER_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                               stream=fp,
                               title=u'博泰自动化测试报告',
                               description=u'主要测试登陆、设置两个模块'
                               )
    runner.run(alltests)
'''