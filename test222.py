#coding=utf-8
'''
Created on 2015年2月28日

@author: xun
'''

from xml.dom import minidom
import xlrd
import os
aa = [{'testsuite': u'Testsuite1', 
       'precondition': [u'Preconditon1', u'Preconditon2', u'Preconditon3'], 
       'importance': [u'1.0', u'2.0', u'3.0'], 
       'execution_type': [u'1.0', u'2.0', u'1.0'], 
       'testcases': [u'Testcase1', u'Testcase2', u'Testcase3'], 
       'steps': [[{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'1.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'1.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'1.0'}, {'action': u'Action4', 'stepid': u'4.0', 'result': u'Result4', 'execution_type': u'1.0'}], [{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'2.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'2.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'2.0'}, {'action': u'Action4', 'stepid': u'4.0', 'result': u'Result4', 'execution_type': u'2.0'}, {'action': u'Action5', 'stepid': u'5.0', 'result': u'Result5', 'execution_type': u'2.0'}], [{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'1.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'1.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'1.0'}, {'action': u'Action4', 'stepid': u'4.0', 'result': u'Result4', 'execution_type': u'1.0'}, {'action': u'Action5', 'stepid': u'5.0', 'result': u'Result5', 'execution_type': u'1.0'}]], 
       'summary': [u'Summary1', u'Summary2', u'Summary3']},
      
       {'testsuite': u'Testsuite2', 
        'precondition': [u'Preconditon4'], 
        'importance': [u'1.0'], 
        'execution_type': [u'2.0'], 
        'testcases': [u'Testcase4'], 
        'steps': [[{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'2.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'2.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'2.0'}]], 
        'summary': [u'Summary4']}]
bb = [{'testsuite': u'Testsuite1', 
       'precondition': [u'Preconditon1', u'Preconditon2', u'Preconditon3'], 
       'importance': [u'1.0', u'2.0', u'3.0'], 
       'execution_type': [u'1.0', u'2.0', u'1.0'], 
       'testcases': [u'Testcase1', u'Testcase2', u'Testcase3'], 
       'steps': [[{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'1.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'1.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'1.0'}, {'action': u'Action4', 'stepid': u'4.0', 'result': u'Result4', 'execution_type': u'1.0'}], [{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'2.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'2.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'2.0'}, {'action': u'Action4', 'stepid': u'4.0', 'result': u'Result4', 'execution_type': u'2.0'}, {'action': u'Action5', 'stepid': u'5.0', 'result': u'Result5', 'execution_type': u'2.0'}], [{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'1.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'1.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'1.0'}, {'action': u'Action4', 'stepid': u'4.0', 'result': u'Result4', 'execution_type': u'1.0'}, {'action': u'Action5', 'stepid': u'5.0', 'result': u'Result5', 'execution_type': u'1.0'}]], 
       'summary': [u'Summary1', u'Summary2', u'Summary3']},
      
       {'testsuite': u'Testsuite2', 
        'precondition': [u'Preconditon4'], 
        'importance': [u'1.0'], 
        'execution_type': [u'2.0'], 
        'testcases': [u'Testcase4'], 
        'steps': [[{'action': u'Action1', 'stepid': u'1.0', 'result': u'Result1', 'execution_type': u'2.0'}, {'action': u'Action2', 'stepid': u'2.0', 'result': u'Result2', 'execution_type': u'2.0'}, {'action': u'Action3', 'stepid': u'3.0', 'result': u'Result3', 'execution_type': u'2.0'}]], 
        'summary': [u'Summary4']}]

cc = [{
"bigsuite":u'bigsuite1', 
"suite":[u'suite1', u'suite2'], 
"cases":[[{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase2",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase3",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'}],[{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'}]]
},

{
"bigsuite":u'bigsuite2',
"suite":[u'suite3', u'suite4'], 
"cases":[[{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'}],[{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'},{"name":u"testcase1",'summary': u'summary','preconditions': u'preconditions', 'importance':  u'1.0'}]]
}]

class exportxml:
    def __init__(self,testdata,outputfolder,filename):
        self.testdata = testdata
        self.output = outputfolder
        self.filename = filename
        
    def export(self):
        print self.testdata
        impl = minidom.getDOMImplementation()
        dom = impl.createDocument(None, None, None)
        inittestsuite = dom.createElement("testsuite")
        inittestsuite.setAttribute("name", "")   
        i=0
        bigsuite_s =[]
        
        while i<len(self.testdata):                        
            bigsuite =  dom.createElement("testsuite")                    
            bigsuite_s.append(bigsuite)
            bigsuite_s[i] =  dom.createElement("testsuite")       
            bigsuite_s[i].setAttribute("name", self.testdata[i].get("bigsuite"))   

            
            
        
 
  
            suite_s = [] 
            
            j=0
            while j<len(self.testdata[i].get("suite")):        
                suite = dom.createElement("testsuite")
                suite_s.append(suite)
                suite_s[j].setAttribute("name", self.testdata[i].get("suite")[j]) 
                print self.testdata[i].get("suite")[j]                                                  
                cases_s =[]
                testcase_s=[]
                summary_s =[]
                preconditions_s =[]
                importance_s =[]

                k = 0
                while k < len(self.testdata[i].get("cases")[j]):
                    print len(self.testdata[i].get("cases")[j])

                    testcase = dom.createElement("testcase")
                    testcase_s.append(testcase)
                    
                    summary = dom.createElement("summary")
                    summary_s.append(summary)
                    preconditions = dom.createElement("preconditions")
                    preconditions_s.append(preconditions)
                    importance = dom.createElement("importance")
                    importance_s.append(importance)
                    
                    testcase_text = dom.createTextNode(self.testdata[i].get("cases")[j][k].get("name"))                    
                    print self.testdata[i].get("cases")[j][k].get("name")
                    summary_text = dom.createTextNode(self.testdata[i].get("cases")[j][k].get("summary"))               
                    preconditions_text = dom.createTextNode(self.testdata[i].get("cases")[j][k].get("preconditions"))
                    importance_text = dom.createTextNode(self.testdata[i].get("cases")[j][k].get("importance"))            
                    
                    testcase_s[k].setAttribute("name", testcase_text)                                                         
                    summary_s[k].appendChild(summary_text)                
                    preconditions_s[k].appendChild(preconditions_text)                
                    importance_s[k].appendChild(importance_text)
                    
                    
                    testcase_s[k].appendChild(summary_s[k])
                    testcase_s[k].appendChild(preconditions_s[k])
                    testcase_s[k].appendChild(importance_s[k])
                    cases_s[j].appe
                    
                    suite_s[j].appendChild(testcase_s[k])
                    
                    
                    k = k+1
                    bigsuite_s[i].appendChild(suite_s[j])
                j = j+1 
            inittestsuite.appendChild(bigsuite_s[i])
            i=i+1    
        dom.appendChild(inittestsuite)
        f=file(self.output+"/"+self.filename+".xml",'w')
        dom.writexml(f,'',' ','\n','utf-8')
        f.close()
        
if __name__ == "__main__":
    a =exportxml(cc,"C:/Users/wangxun/Desktop","222")
    a.export()