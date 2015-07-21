
import xlrd
import exportxml


edata = xlrd.open_workbook('D:/testexcel.xls')
table = edata.sheet_by_name("Sheet1")
def suitedis():
    j=1
    dis =[]
    while j<table.nrows:
        if table.cell(j,0).value:
            dis.append(j)
        j=j+1
    dis.append(table.nrows)
    print dis
    return dis

def casedis():
    j=1
    dis =[]
    while j<table.nrows:
        if table.cell(j,6).value ==1.0:
            dis.append(j)
        j=j+1
    dis.append(table.nrows)
    print dis
    return dis
    
def datastep():
    a = casedis()
    test =[]
    i =0
    while i<len(a)-1:
        test.append(data.read()[6][a[i]-1:a[i+1]-1])
        i=i+1
    return test


    


data = exportxml.readexcel("testexcel.xls")
print data.read()[0]

a = suitedis()
b = casedis()
print a
c = datastep()
print len(c)
print len(data.read()[1])
print len(data.read()[2])
print len(data.read()[3])
print len(data.read()[4])
print len(data.read()[5])
i = 1

    