#coding=utf-8
'''
Created on 2014-9-22

@author: xun
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep
import random
import string

class test(unittest.TestCase):
    def setUp(self):
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])
        self.driver.implicitly_wait(30)
        self.base_url = "http://42.96.155.222:8888/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def tablelasttrcount(self,css):
        a = str(css)
        b = a.find('tr:')
        c = a.find('(',b,-1)
        d = a.find(')',b,-1)        
        e = a[c+1:d]      
        f = string.atoi(e)        
        i = 2

        while i<f:
            g = a[:c+1] +str(i) + a[d:]
            i +=1
            try:
                self.driver.find_element_by_css_selector(g)
                continue
            except:
                if i-2>1:
                    return i-2
                    break
                else:
                    return 2
                    break


            
                    


            

        
            

        
    def enterverison(self):    
        self.driver.get(self.base_url + "login?next=%2F")
        self.driver.find_element_by_name('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()
        self.driver.find_element_by_css_selector('#li_id_release').click()                
        
    def entermanagement(self): 
        self.driver.get(self.base_url + "login?next=%2F")
        self.driver.find_element_by_name('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()        
        self.driver.find_element_by_css_selector('#li_id_user').click()      
           
    def test_login(self):
        self.driver.get(self.base_url + "login?next=%2F")                   
        self.driver.find_element_by_name('account').clear()
        self.driver.find_element_by_name('account').send_keys('admin')
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]') .click()       
        print '是否验证密码为空:','Incorrect account or password.' in self.driver.find_element_by_css_selector('body').text  
        self.driver.find_element_by_name('account').clear()        
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()        
        print '是否验证账号为空:','Incorrect account or password.' in self.driver.find_element_by_css_selector('body').text         
        self.driver.find_element_by_name('account').clear()
        self.driver.find_element_by_name('account').send_keys('admin1' )
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys('admin1')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()
        sleep(1)       
        print '是否验证无效账号或密码:','Incorrect account or password.' in self.driver.find_element_by_css_selector('body').text 
        self.driver.get(self.base_url + "login?next=%2F")
        self.driver.find_element_by_name('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()
        print '检查是否登陆成功：' ,'Statistics' == self.driver.title

        
    
    def test_publishrelease(self):
        self.enterverison()      
        sleep(1)
        version = self.driver.find_element_by_css_selector('#release_version')
        platform = self.driver.find_element_by_css_selector('#release_platform')
        url = self.driver.find_element_by_css_selector('#release_url')
        notes = self.driver.find_element_by_css_selector('#release_notes')
        publish = self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div.addsubmit > button')       
        a = random.randrange(1,9)
        b = random.randrange(1,9)
        c = random.randrange(1,9)
        d = random.randrange(1,9)
        e = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d) 
        if e in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text:
            version.send_keys(e)
            url.send_keys('http://42.96.155.222:8888/admin/release')
            self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > button').click()
            print '检查是否验证URL格式：', 'Pass.' in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > span.verify_1.hide').text
            notes.send_keys(u'测试'*100)
            Select(platform).select_by_index(1)
            publish.click()
            sleep(2)
            print '检查是否验证重复版本：','Version already exists' in self.driver.find_element_by_css_selector('div.modal-dialog').text
            sleep(1)
            ok = self.driver.find_element_by_css_selector(' div > div > div.modal-footer > div > div > button')
            ok.click()
        else:
            version.send_keys(e)
            url.send_keys('http://42.96.155.222:8888/admin/release')
            self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > button').click()
            print '检查是否验证URL格式：', 'Pass.' in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > span.verify_1.hide').text
            notes.send_keys(u'测试'*100)
            Select(platform).select_by_index(1)
            publish.click()
            sleep(1)
            print '检查是否发布版本成功：',e in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text
            sleep(1)
            self.driver.find_element_by_css_selector('#release_version').send_keys(e)
            self.driver.find_element_by_css_selector('#release_url').send_keys('http://42.96.155.222:8888/admin/release')
            self.driver.find_element_by_css_selector('#release_notes').send_keys(u'测试'*100)
            Select(self.driver.find_element_by_css_selector('#release_platform')).select_by_index(1)
            self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div.addsubmit > button').click()
            print '检查是否验证重复版本：','Version already exists' in self.driver.find_element_by_css_selector('div.modal-dialog').text
            sleep(1)
            ok = self.driver.find_element_by_css_selector(' div > div > div.modal-footer > div > div > button')
            ok.click()
    
    def test_zdeleteversion(self):
        self.enterverison()
        sleep(1)
        try:
            a = self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(1)').text
            self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > button').click()
            sleep(1)
            self.driver.find_element_by_css_selector('#myModal > div.modal-footer > a.btn.btn-info').click()
            sleep(1)
            print '检查是否成功删除版本', a not in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text
        except:
            print '版本列表没有版本'  
            
    def test_editversion(self):
        self.enterverison()
        sleep(1)
        try:
            a = self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(4)').text
            b = a+'123'
            self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > button').click()
            sleep(1)
            self.driver.find_element_by_css_selector('#url_edit').clear()
            self.driver.find_element_by_css_selector('#url_edit').send_keys(b)
            self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-body > button').click()
            print '检查编辑时是否成功验证URL格式：', 'Pass.' in self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-body > span.edit_verify_1.hide').text
            self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-footer > a.btn.btn-info').click()
            sleep(1)
            print '检查是否编辑成功：', b in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(4)').text
        except:
            print '版本列表没有版本'
            
    def test_newuser(self):
        self.entermanagement()
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > div > div.float_right > button').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#input_account').clear()
        a = str(random.randrange(10, 10000000))
        self.driver.find_element_by_css_selector('#input_account').send_keys(a)
        select = self.driver.find_element_by_css_selector('#select_role')
        Select(select).select_by_index(3)
        self.driver.find_element_by_css_selector('#myModal2 > div.modal-footer > a.btn.btn-info').click()
        if 'Account already exists' in self.driver.find_element_by_css_selector('#myModal2 > div.modal-body > div > form > table > tbody').text:
            sleep(1)
            print '检查是否已存在该账号：', 'Account already exists' in self.driver.find_element_by_css_selector('#myModal2 > div.modal-body > div > form > table').text
        else:
            sleep(1)
            print '检查是否成功创建账号：', a in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text
            self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > div > div.float_right > button').click()
            sleep(1)
            self.driver.find_element_by_css_selector('#input_account').clear()
            self.driver.find_element_by_css_selector('#input_account').send_keys(a)
            self.driver.find_element_by_css_selector('#myModal2 > div.modal-footer > a.btn.btn-info').click()
            sleep(1)
            print '检查是否已存在该账号：', 'Account already exists' in self.driver.find_element_by_css_selector('#myModal2 > div.modal-body > div > form > table').text
            
        
    def test_zdeleteuser(self):
        self.entermanagement()
        a = self.tablelasttrcount('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(200) > td:nth-child(7) > button')
        deletecss = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(a) + ') > td:nth-child(7) > button'
        usercss = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(a) + ') > td:nth-child(1)'
        u = self.driver.find_element_by_css_selector(usercss).text
        self.driver.find_element_by_css_selector(deletecss).click()
        sleep(1)
        self.driver.find_element_by_css_selector('#DelUserModal > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        print '检查是否删除用户：' , u not in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text
        
    def test_clearfeedback(self):
        self.entermanagement()
        selectversion = self.driver.find_element_by_css_selector('#clearSelectVersion')
        Select(selectversion).select_by_visible_text('ALL')
        selectcontent = self.driver.find_element_by_css_selector('#clearSelectType')
        Select(selectcontent).select_by_visible_text('Feedbacks')
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(3) > div > div > div > button').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#myModalalldel > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#li_id_feedbacks').click()
        sleep(1)
        print '检查是否清空feedbacks信息：' , '1' not in self.driver.find_element_by_css_selector('#table-javascript > tbody').text

    def test_signout(self):
        self.entermanagement()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup > button').click()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup.open > ul > li:nth-child(2)').click()
        sleep(1)
        print '检查是否退出成功：', 'AppLink™ Emulator' in self.driver.find_element_by_css_selector('body').text
        
    def test_asetting(self):
        self.entermanagement()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup > button').click()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup.open > ul > li:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#username').clear()
        self.driver.find_element_by_css_selector('#username').send_keys('admintest')
        self.driver.find_element_by_css_selector('#password1').clear()
        self.driver.find_element_by_css_selector('#password1').send_keys('admin')
        self.driver.find_element_by_css_selector('#password2').clear()
        self.driver.find_element_by_css_selector('#password2').send_keys('admin')
        self.driver.find_element_by_css_selector('#email').clear()
        self.driver.find_element_by_css_selector('#email').send_keys('59853844@qq.com')
        self.driver.find_element_by_css_selector('body > div.mainwrap_forgot > div > div:nth-child(2) > div.addsubmit.addlist > button.btn.btn-default.btn-info').click()
        print '检查是否设置成功：', 'AppLink™ Emulator' in self.driver.find_element_by_css_selector('body').text
        

        
        

        
            
        


        
        
        
        



            
 
            
            
        

        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert() 
        except : return False
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
    suite = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner(verbosity=2).run(suite)

