
from xml.dom import minidom
import xlrd
'''dom = minidom.parse('C:/Users/wangxun/Downloads/testcases.xml')
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
bb = root.getElementsByTagName('testcase')
b = bb[0]
print b.nodeName
print b.getAttribute("name")
cc = root.getElementsByTagName('actions')
c = cc[0]
print c.firstChild.data
'''
from _mysql import NULL


class exportxml:
    def __init__(self,testdata):
        self.testdata = testdata
        
    def export(self):
        impl = minidom.getDOMImplementation()
        dom = impl.createDocument(None, None, None)
        testsuite =  dom.createElement("testsuite")
        inittestsuite = dom.appendChild(testsuite)
        i=0
        testsuite_s =[]
        while i<len(self.testdata):
            
            
            testsuite =  dom.createElement("testsuite")
        
            inittestsuite.setAttribute("name", "")   
            testsuite_s.append(testsuite)
            testsuite_s[i] =  dom.createElement("testsuite")
            print len(self.testdata)
            print 111
            
        
        
        
        
        
            testsuite_s[i].setAttribute("name", self.testdata[i].get("testsuite"))   
            testcase_s=[]
            summary_s =[]
            preconditions_s =[]
            execution_type_s =[]
            importance_s =[]
            steps_s=[]
            
            j=0
            while j<len(self.testdata[i].get("testcases")):
        
                print self.testdata[i].get("summary")[j]
                testcase = dom.createElement("testcase")
                testcase_s.append(testcase)
                summary = dom.createElement("summary")
                summary_s.append(summary)
                preconditions = dom.createElement("preconditions")
                preconditions_s.append(preconditions)
                execution_type = dom.createElement("execution_type")
                execution_type_s.append(execution_type)
                importance = dom.createElement("importance")
                importance_s.append(importance)
                steps = dom.createElement("steps")
                steps_s.append(steps)
                
        
                
                print  len(testcase_s)
                print j
                print len(self.testdata[i].get("steps")[j])
                print self.testdata[i].get("steps")[j][1].get("action")
                testcase_s[j].setAttribute("name", self.testdata[i].get("testcases")[j])
        
            
                
            
            
            
            
                summary_text = dom.createTextNode(self.testdata[i].get("summary")[j])
                precondition_text = dom.createTextNode(self.testdata[i].get("precondition")[j])
                execution_type_text = dom.createTextNode(self.testdata[i].get("execution_type")[j])
                importance_text = dom.createTextNode(self.testdata[i].get("importance")[j])
            
                summary_s[j].appendChild(summary_text)
                
                preconditions_s[j].appendChild(precondition_text)
                
                execution_type_s[j].appendChild(execution_type_text)
                
                importance_s[j].appendChild(importance_text)
                step_s=[]
                step_number_s =[]
                actions_s =[]
                expectedresults_s =[]
                step_execution_type_s =[]
                testcase_s[j].appendChild(summary_s[j])
                testcase_s[j].appendChild(preconditions_s[j])
                testcase_s[j].appendChild(execution_type_s[j])
                testcase_s[j].appendChild(importance_s[j])
            
                k=0
                while k<len(self.testdata[i].get("steps")[j]):
                    print "343434343"
                    print k
                    print j
                    print i
                    step = dom.createElement("step")
                    step_number = dom.createElement("step_number")
                    actions = dom.createElement("actions")
                    expectedresults = dom.createElement("expectedresults")
                    step_execution_type = dom.createElement("execution_type")
        
                    
                    step_s.append(step)
                    step_number_s.append(step_number)
                    actions_s.append(actions)
                    expectedresults_s.append(expectedresults)
                    step_execution_type_s.append(step_execution_type)
        
                    step_number_text = dom.createTextNode(self.testdata[i].get("steps")[j][k].get("stepid"))
                    actions_text = dom.createTextNode(self.testdata[i].get("steps")[j][k].get("action"))
                    print self.testdata[i].get("steps")[j][k].get("action")
                    expectedresults_text = dom.createTextNode(self.testdata[i].get("steps")[j][k].get("result"))
                    step_execution_type_text = dom.createTextNode(self.testdata[i].get("steps")[j][k].get("execution_type"))
                    
                    step_number_s[k].appendChild(step_number_text)
                    actions_s[k].appendChild(actions_text)
                    expectedresults_s[k].appendChild(expectedresults_text)
                    step_execution_type_s[k].appendChild(step_execution_type_text)
                
                    step_s[k].appendChild( step_number_s[k])
                    step_s[k].appendChild(actions_s[k])
                    step_s[k].appendChild(expectedresults_s[k])
                    step_s[k].appendChild(step_execution_type_s[k])
                
                    steps_s[j].appendChild(step_s[k])
                    testcase_s[j].appendChild(steps_s[j])
                    
        
          
                    
                    testsuite_s[i].appendChild(testcase_s[j])
                    
        
                    k=k+1
        
                j=j+1
        
            inittestsuite.appendChild(testsuite_s[i])
        
        
            i=i+1
    
        dom.appendChild(inittestsuite)
        f=file('D:/skills.xml','w')
        dom.writexml(f,'',' ','\n','utf-8')
        f.close()

class readexcel:
    def __init__(self,testexcel):
        self.testexcel = testexcel
        data = xlrd.open_workbook(self.testexcel)
        self.table = data.sheet_by_name("Sheet1")
        self.testdata = []
        self.testsuites = []
        self.testcases =[]
        self.summary =[]
        self.preconditon =[]
        self.casetype = []
        self.importance =[]
        self.steps = []
        self.casestep = []
        
        
        
        
        
        
    def read(self):



        data =[]
        print self.table.nrows
        print self.table.ncols
        print self.table.cell(0,0).value
        print self.table.cell(1,0).value
        print self.table.cell(2,0).value
        print self.table.cell(3,0).value
        i =1
        while i<self.table.nrows:
            step ={}
            testsuite = {}
            if self.table.cell(i,0).value and self.table.cell(i,1).value and self.table.cell(i,6).value:
                testsuite.setdefault("testsuite",self.table.cell(i,0).value)
                self.testcases.append(self.table.cell(i,1).value)
                self.summary.append(self.table.cell(i,2).value)
                self.preconditon.append(self.table.cell(i,3).value)
                self.casetype.append(self.table.cell(i,4).value)
                self.importance.append(self.table.cell(i,5).value)
                step.setdefault("stepid",self.table.cell(i,6).value)
                step.setdefault("action",self.table.cell(i,7).value)
                step.setdefault("result",self.table.cell(i,8).value)
                step.setdefault("execution_type",self.table.cell(i,9).value)
                self.steps.append(step)
                self.testsuites.append(testsuite)
                
                
            if not self.table.cell(i,0).value and not self.table.cell(i,1).value and self.table.cell(i,6).value:
                
                step.setdefault("stepid",self.table.cell(i,6).value)
                step.setdefault("action",self.table.cell(i,7).value)
                step.setdefault("result",self.table.cell(i,8).value)
                step.setdefault("execution_type",self.table.cell(i,9).value)
                self.steps.append(step)
                
            if not self.table.cell(i,0).value and self.table.cell(i,1).value and self.table.cell(i,6).value:
                
                
                self.testcases.append(self.table.cell(i,1).value)
                self.summary.append(self.table.cell(i,2).value)
                self.preconditon.append(self.table.cell(i,3).value)
                self.casetype.append(self.table.cell(i,4).value)
                self.importance.append(self.table.cell(i,5).value)
                step.setdefault("stepid",self.table.cell(i,6).value)
                step.setdefault("action",self.table.cell(i,7).value)
                step.setdefault("result",self.table.cell(i,8).value)
                step.setdefault("execution_type",self.table.cell(i,9).value)
                self.steps.append(step)
            i=i+1

        data.append(self.testsuites)
        data.append(self.testcases)
        data.append(self.summary)
        data.append(self.preconditon)
        data.append(self.casetype)
        data.append(self.importance)
        data.append(self.steps)
        data.append(self.casestep)
        return data

        
    def casedis(self):
        j=1
        dis =[]
        while j<self.table.nrows:
            if self.table.cell(j,6).value ==1.0:
                dis.append(j)
            j=j+1
        dis.append(self.table.nrows)
        print dis
        return dis
    
    def suitedis(self):
        j=1
        dis =[]
        while j<self.table.nrows:
            if self.table.cell(j,0).value:
                dis.append(j)
            j=j+1
        dis.append(self.table.nrows)
        print dis
        return dis
    
        
    def teststep(self):
        a = [1, 4, 6, 9, 11]
        b = [1, 6, 11]
        test =[]
        i =0
        while i<len(a)-1:
            test.append(self.steps[a[i]-1:a[i+1]-1])
            i=i+1
        print test
        return test
        
            

        



if __name__ == "__main__":
    testdata = [{"testsuite":"suite1","testcases":["testcase1","testcase2"],"summary":["summary1","summary2"]
             ,"precondition":["pre1","pre2"],"execution_type":["1","2"],"importance":["1","2"]
             ,"steps":[[{"stepid":"1","action":"action1","result":"result1","execution_type":"1"},
                       {"stepid":"2","action":"action2","result":"result2","execution_type":"2"}],
                       [{"stepid":"1","action":"action1","result":"result1","execution_type":"1"},
                       {"stepid":"2","action":"action2","result":"result2","execution_type":"2"}]]},
            {"testsuite":"suite2","testcases":["testcase1","testcase2"],"summary":["summary1","summary2"]
             ,"precondition":["pre1","pre2"],"execution_type":["1","2"],"importance":["1","2"]
             ,"steps":[[{"stepid":"1","action":"action1","result":"result1","execution_type":"1"},
                       {"stepid":"2","action":"action2","result":"result2","execution_type":"2"}],
                       [{"stepid":"1","action":"action1","result":"result1","execution_type":"1"},
                       {"stepid":"2","action":"action2","result":"result2","execution_type":"2"}]]}]
    aa =exportxml(testdata)
#    aa.export()
    bb = readexcel('D:/testexcel.xls')
    bb.read()
#    bb.casedis()
#    bb.suitedis()
#    bb.casestep()
    bb.test()