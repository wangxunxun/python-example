
import xlrd
import exportxml
edata = xlrd.open_workbook('testexcel.xls')
table = edata.sheet_by_name("Sheet1")
class testtest:
    
    def suitedis(self):
        
        j=1
        dis =[]
        

        while j<table.nrows:
            if table.cell(j,0).value:
                dis.append(j)
            j=j+1
        dis.append(table.nrows)
        return dis
    
    def casedis(self):
        j=1
        dis =[]
        while j<table.nrows:
            if table.cell(j,6).value ==1.0:
                dis.append(j)
            j=j+1
        dis.append(table.nrows)
        return dis
  
    def datastep(self):
        a = self.casedis()
        test =[]
        i =0
        while i<len(a)-1:
            test.append(data.read()[6][a[i]-1:a[i+1]-1])
            i=i+1
        return test
    
    def casecount(self,i,j):
        k=1
        start =0
        end =0
        while k<i:
            if table.cell(k,6).value ==1.0:
                start = start +1
            k=k+1
        l=1
        while l<j:
            if table.cell(l,6).value ==1.0:
                end = end +1
            l=l+1

        return end - start
    
    def datacase(self):
        test =[]
        a = self.suitedis()
        b = self.casedis()


        i =0
        while i<len(a)-1:
            bb=self.casecount(a[i], a[i+1])
            test.append(bb)
            
            
            i=i+1
        return test
        
    def case(self):
        a =self.datacase()

        i=0
        allcases=[]
        
        while i<len(a):
            if i==0:
                cases = []
                case = data.read()[1][i:a[i]]
                summary = data.read()[2][i:a[i]]
                precondition = data.read()[3][i:a[i]]
                execution_type = data.read()[4][i:a[i]]
                importance = data.read()[5][i:a[i]]
                steps = test.datastep()[i:a[i]]
                cases.append(case)
                cases.append(summary)
                cases.append(precondition)
                cases.append(execution_type)
                cases.append(importance)
                cases.append(steps)
                
                allcases.append(cases)
                
            else:
                cases = []
                case = data.read()[1][a[i-1]:a[i-1]+a[i]]
                summary = data.read()[2][a[i-1]:a[i-1]+a[i]]
                precondition = data.read()[3][a[i-1]:a[i-1]+a[i]]
                execution_type = data.read()[4][a[i-1]:a[i-1]+a[i]]
                importance = data.read()[5][a[i-1]:a[i-1]+a[i]]
                steps = test.datastep()[a[i-1]:a[i-1]+a[i]]                                
                cases.append(case)
                cases.append(summary)
                cases.append(precondition)
                cases.append(execution_type)
                cases.append(importance)
                cases.append(steps)                
                allcases.append(cases)                            
            i=i+1
        return allcases

    def testsuite(self):
        i = 0
        suite =[]
        test = self.case()
        print data.read()[0][0].get("testsuite")
        while i<len(data.read()[0]):
            aa = {}
            aa.setdefault("testsuite",data.read()[0][i].get("testsuite"))
            aa.setdefault("testcases",test[i][0])
            aa.setdefault("summary",test[i][1])
            aa.setdefault("precondition",test[i][2])
            aa.setdefault("execution_type",test[i][3])
            aa.setdefault("importance",test[i][4])
            aa.setdefault("steps",test[i][5])
            suite.append(aa)
            i=i+1
        return suite
            
        

if __name__ == "__main__":
    data = exportxml.readexcel("testexcel.xls")
#    data.returndata()
    test = testtest()
    

    bb = test.testsuite()
    print bb
'''    
    print test.case()
    print test.case()[0]
    print test.case()[1]
    print len(test.case())
    print data.read()[0]
    print data.read()[1]    
    print data.read()[2]    
    print data.read()[3]    
    print data.read()[4]    
    print data.read()[5]   
#    print data.read()[6]   
#    print len(data.read()[6])
    print test.datastep()
    print len(test.datastep())
'''
 
    
    
#    print test.datastep()
#    print len(test.datastep())


'''
print data.returndata()[0]
print data.returndata()[1]
print data.returndata()[2]
print data.returndata()[3]
print data.returndata()[4]
print data.returndata()[5]
'''
'''
print len(c)
print len(data.read()[1])
print len(data.read()[2])
print len(data.read()[3])
print len(data.read()[4])
print len(data.read()[5])
i = 1
'''
    