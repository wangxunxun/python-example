
import xlrd
import exportxml


data = xlrd.open_workbook('D:/testexcel.xls')
table = data.sheet_by_name("Sheet1")
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
    
def teststep():
    a = [1, 4, 6, 9, 11]
    b = [1, 6, 11]


data = exportxml.readexcel("testexcel.xls")
print data.read()[0]

a = suitedis()
b = casedis()
print a

i = 1

    