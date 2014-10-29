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
import HTMLTestRunner
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class basictestcase(unittest.TestCase):
    def setUp(self):
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="/Users/wangxun/Documents/chromedriver", service_args=["--verbose", "--log-path=D:\\qc1.log"])        
#        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])
#        self.driver = webdriver.Remote("http://localhost:8080/wd/hub", webdriver.DesiredCapabilities.ANDROID)
        self.driver.implicitly_wait(30)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://106.186.19.168:8888/"
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
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()
        self.driver.find_element_by_css_selector('#li_id_release').click()           
        self.wait.until(EC.title_is('Release Control'))  
        
    def entermanagement(self): 
        self.driver.get(self.base_url + "login?next=%2F")
        self.driver.find_element_by_name('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]').click()        
        self.driver.find_element_by_css_selector('#li_id_user').click()  
        self.wait.until(EC.title_is('Management'))
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    




class login(basictestcase):
    
    def login(self,account,password):
        self.driver.get(self.base_url + "login?next=%2F")                   
        self.driver.find_element_by_name('account').clear()
        self.driver.find_element_by_name('account').send_keys(account)
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_css_selector('div.login_button > input[value="Login"]') .click()  
                   
    def test_nopassword(self):
        u'''密码为空'''
        self.login('admin', '')      
        self.assertIn('Please enter the password.',self.driver.find_element_by_css_selector('body').text)       

    def test_noaccount(self):
        u'''账号为空'''
        self.login('', '123456')   
        self.assertIn('Please enter the username.',self.driver.find_element_by_css_selector('body').text)   
        
    def test_invalidaccountorpassword(self): 
        u'''无效的账号或密码'''      
        self.login('admin2', 'admin2')
        self.assertIn('Incorrect username or password.',self.driver.find_element_by_css_selector('body').text) 
               
    def test_loginsuccess(self):
        u'''登陆成功'''
        self.login('admin', '123456')
        self.assertIn('Statistics', self.driver.title)  
        
class releasecontrol(basictestcase):
    a = random.randrange(1,9)
    b = random.randrange(1,9)
    c = random.randrange(1,9)
    d = random.randrange(1,9)
    versionnumber = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d) 
    
    
    def publishversion(self,version,platformname,url,notes):
        platform = self.driver.find_element_by_css_selector('#release_platform')  
        self.driver.find_element_by_css_selector('#release_version').send_keys(version)
        self.driver.find_element_by_css_selector('#release_url').send_keys(url)
        self.driver.find_element_by_css_selector('#release_notes').send_keys(notes)
        Select(platform).select_by_visible_text(platformname)
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div.addsubmit > button').click()
        sleep(1)

    def editversion(self,url,notes):
        self.url = url
        self.notes = notes
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > button').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#editReleaseModal > div.modal-footer > a.btn.btn-info')))
        if self.url:
            self.driver.find_element_by_css_selector('#url_edit').clear()
            self.driver.find_element_by_css_selector('#url_edit').send_keys(self.url)
        if self.notes:
            self.driver.find_element_by_css_selector('#notes_edit').clear()
            self.driver.find_element_by_css_selector('#notes_edit').send_keys(self.notes)
        self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
                        
    def test_publishnewversion(self):
        u'''发布新版本'''
        self.enterverison()   
        while self.versionnumber in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text:
            self.versionnumber += '1'    

        self.publishversion(self.versionnumber, 'Mac', 'http://106.186.19.168:8888/admin/release', u'测试'*20)
        self.assertIn(self.versionnumber, self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text)
            
    def test_q_publishexistedversion(self):
        u'''发布已存在的版本'''
        self.enterverison()     
        self.publishversion(self.versionnumber, 'Mac', 'http://106.186.19.168:8888/admin/release', '3333')
        self.assertIn('Version already exists', self.driver.find_element_by_css_selector('div > div > div.modal-body > div > div').text)
    
    def test_checkURL(self):  
        u'''验证URL功能'''
        self.enterverison()      
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#tab1 > div:nth-child(1) > div > table > tbody"),'Release')) 
        self.driver.find_element_by_css_selector('#release_url').send_keys('http://42.96.155.222:8888/admin/release')
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > button').click()
        self.assertIn('Pass.', self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > span.verify_1.hide').text)
        print u'成功验证发布页面正确URL格式'
        self.driver.find_element_by_css_selector('#release_url').clear()
        self.driver.find_element_by_css_selector('#release_url').send_keys('8888/admin/release')
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > button').click()          
        self.assertIn('Fail.', self.driver.find_element_by_css_selector('#tab1 > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.float_left.forminput_div > span.verify_2.hide').text)    
        print u'成功验证错误URL格式'
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > button').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#editReleaseModal > div.modal-footer > a.btn.btn-info')))
        self.driver.find_element_by_css_selector('#url_edit').clear()      
        self.driver.find_element_by_css_selector('#url_edit').send_keys('http://42.96.155.222:8888/admin/release') 
        self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-body > button').click()
        self.assertIn('Pass.', self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-body > span.edit_verify_1.hide').text)    
        print u'成功验证编辑页面正确URL格式'
        self.driver.find_element_by_css_selector('#url_edit').clear()      
        self.driver.find_element_by_css_selector('#url_edit').send_keys('8888/admin/release') 
        self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-body > button').click()     
        self.assertIn('Fail.', self.driver.find_element_by_css_selector('#editReleaseModal > div.modal-body > span.edit_verify_2.hide').text)    
        print u'成功验证编辑页面错误URL格式'       
                           
    def test_r_editversion(self):
        u'''编辑版本'''
        self.enterverison()
        self.editversion('http://106.186.19.168:8888/admin/release', '1111')
        self.assertIn('http://106.186.19.168:8888/admin/release', self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(4)').text)
    
    def test_z_deleteversion(self):
        u'''删除版本'''        
        self.enterverison()
        a = self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(1)').text
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > button').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#myModal > div.modal-footer > a.btn.btn-info')))        
        self.driver.find_element_by_css_selector('#myModal > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        self.assertNotIn(a, self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text)            
           
class management(basictestcase):
    a = str(random.randrange(10, 10000000))
    
    def newuser(self,account,role):
        self.account = account
        self.role = role
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > div > div.float_right > button').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#myModal2 > div.modal-footer > a.btn.btn-info')))
        self.driver.find_element_by_css_selector('#input_account').clear()
        self.driver.find_element_by_css_selector('#input_account').send_keys(self.account)
        select = self.driver.find_element_by_css_selector('#select_role')
        Select(select).select_by_visible_text(self.role)
        self.driver.find_element_by_css_selector('#myModal2 > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        
    def edituser(self,name,email,role):
        self.name = name
        self.email = email
        self.role = role
        lastrownum = self.tablelasttrcount('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(200) > td:nth-child(6) > button')
        editcss = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(lastrownum) + ') > td:nth-child(6) > button'
        self.driver.find_element_by_css_selector(editcss).click()   
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#EditUserModal > div.modal-footer > a.btn.btn-info')))
        self.driver.find_element_by_css_selector('#edit_name').clear()
        self.driver.find_element_by_css_selector('#edit_name').send_keys(self.name)     
        self.driver.find_element_by_css_selector('#edit_email').clear()
        self.driver.find_element_by_css_selector('#edit_email').send_keys(self.email)
        selectrole = self.driver.find_element_by_css_selector('#edit_role')
        Select(selectrole).select_by_visible_text(self.role)
        self.driver.find_element_by_css_selector('#EditUserModal > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        return lastrownum        
            
    def test_newuser(self):
        u'''新建用户'''
        self.entermanagement()

        while self.a in self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text:
            self.a +='1'
            
        self.newuser(self.a, 'Others')
        self.assertIn(self.a, self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text)
      
    def test_o_newexisteduser(self):
        u'''新建已存在的用户'''
        self.entermanagement()        
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > div > div.float_right > button').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#input_account').clear()
        self.driver.find_element_by_css_selector('#input_account').send_keys(self.a)
        self.driver.find_element_by_css_selector('#myModal2 > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        self.assertIn('Account already exists', self.driver.find_element_by_css_selector('#myModal2 > div.modal-body > div > form > table').text)

    def test_p_edituesr(self):
        u'''编辑用户'''
        self.entermanagement()
        self.lastrownum = self.edituser('haha', '59853844@qq.com', 'Others')
        namecss = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(self.lastrownum) + ') > td:nth-child(2)'
        self.checkname = self.driver.find_element_by_css_selector(namecss).text
        lastrow = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(self.lastrownum) +  ')'
        self.assertIn(self.checkname, self.driver.find_element_by_css_selector(lastrow).text )                
        
    def test_z_deleteuser(self):
        u'''删除已存在的用户'''
        self.entermanagement()
        self.lastrownum = self.tablelasttrcount('#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(200) > td:nth-child(7) > button')
        deletecss = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(self.lastrownum) + ') > td:nth-child(7) > button'
        usercss = '#tab1 > div:nth-child(1) > div > table > tbody > tr:nth-child(' + str(self.lastrownum) + ') > td:nth-child(1)'
        u = self.driver.find_element_by_css_selector(usercss).text
        self.driver.find_element_by_css_selector(deletecss).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#DelUserModal > div.modal-footer > a.btn.btn-info')))
        self.driver.find_element_by_css_selector('#DelUserModal > div.modal-footer > a.btn.btn-info').click()
        sleep(1)
        self.assertNotIn(u, self.driver.find_element_by_css_selector('#tab1 > div:nth-child(1) > div > table').text)    

class setting(basictestcase):
    def editinformation(self,name,password,repassword,email):
        self.name = name
        self.password = password
        self.repassword = repassword
        self.email = email
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup > button').click()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup.open > ul > li:nth-child(1)').click()        
        self.driver.find_element_by_css_selector('#username').clear()
        self.driver.find_element_by_css_selector('#username').send_keys(self.name)
        self.driver.find_element_by_css_selector('#password1').clear()
        self.driver.find_element_by_css_selector('#password1').send_keys(self.password)
        self.driver.find_element_by_css_selector('#password2').clear()
        self.driver.find_element_by_css_selector('#password2').send_keys(self.repassword)
        self.driver.find_element_by_css_selector('#email').clear()
        self.driver.find_element_by_css_selector('#email').send_keys(self.email)        
        self.driver.find_element_by_css_selector('body > div.wrapwidth.indexmargin > div > div > div > div:nth-child(2) > div.addsubmit.addlist > button.btn.btn-default.btn-info').click()    
    
    def test_editPersonalInformation(self):
        u'''编辑用户信息'''
        self.entermanagement()
        self.editinformation('troy', '123456', '123456', '59853844@qq.com')
        self.assertIn(u'AppLink™ Emulator', self.driver.find_element_by_css_selector('body').text)

    def test_signout(self):
        u'''注销'''
        self.entermanagement()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup > button').click()
        self.driver.find_element_by_css_selector('#top > div > div.btn-group.float_right.menugroup.open > ul > li:nth-child(2)').click()
        sleep(1)
        self.assertIn(u'AppLink™ Emulator', self.driver.find_element_by_css_selector('body').text)
        

                                                                            
class feedback(basictestcase):
    
    def clear(self,status,item):
        self.status = status
        self.item = item
        selectversion = self.driver.find_element_by_css_selector('#clearSelectVersion')
        Select(selectversion).select_by_visible_text(self.status)    
        selectcontent = self.driver.find_element_by_css_selector('#clearSelectType')
        Select(selectcontent).select_by_visible_text(item)
        self.driver.find_element_by_css_selector('#tab1 > div:nth-child(3) > div > div > div > button').click()      
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#myModalalldel > div.modal-footer > a.btn.btn-info')))   
        self.driver.find_element_by_css_selector('#myModalalldel > div.modal-footer > a.btn.btn-info').click()   
                        
    def test_clearfeedback(self):
        u'''清空所有feedback'''
        self.entermanagement()
        self.clear('ALL', 'Feedbacks')
        sleep(1)
        self.driver.find_element_by_css_selector('#li_id_feedbacks').click()
        self.wait.until(EC.title_is('Feedbacks'))

        print u'检查是否清空feedbacks信息：' , '1' not in self.driver.find_element_by_css_selector('#table-javascript > tbody').text

        


        
            


if __name__ == "__main__":
    suite_setting = unittest.TestLoader().loadTestsFromTestCase(setting)
    suite_login = unittest.TestLoader().loadTestsFromTestCase(login)
    suite_releasecontrol = unittest.TestLoader().loadTestsFromTestCase(releasecontrol)
    suite_management = unittest.TestLoader().loadTestsFromTestCase(management)
    suite_feedback = unittest.TestLoader().loadTestsFromTestCase(feedback)
    alltests = unittest.TestSuite([suite_login,suite_setting,suite_releasecontrol,suite_management,suite_feedback])

    unittest.TextTestRunner(verbosity=2).run(alltests)
'''
    filename = '/Users/wangxun/Documents/ALE_SERVER_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
#    filename = 'D:/autotestreport/ALE_SERVER_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                               stream=fp,
                               title='ALE server',
                               description='Report_description'
                               )
    runner.run(alltests)
'''