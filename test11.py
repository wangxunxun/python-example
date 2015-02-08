import MySQLdb
import string
sql = """CREATE TABLE EMPLOYEE1 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )""" 
sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
sql2 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
       
       
sql3 = "INSERT INTO EMPLOYEE(FIRST_NAME,\
         LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d')"  
param = (('Mac', 'Mohan', 20, 'M', 20001), ('Mac', 'Mohan', 20, 'M', 20001), ('Mac', 'Mohan', 20, 'M', 20002))  

sql4= "INSERT INTO MESSAGE(ID, \
       TOID, QUNID, NICKNAME, MESSAGE) \
       VALUES ('%d', '%d', '%d', '%s', '%s' )" %        (454, 666, 45, '454', '5656')   


createteble = """CREATE TABLE MESSAGE (
         ID  INT,
         TOID INT, 
         QUNID INT, 
         NICKNAME  CHAR(20),
         MESSAGE CHAR(40)
         )"""   
    
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',port=3306)
    cur=conn.cursor()
    try:
        if cur.execute('show tables like "message"') == 0:
            cur.execute(createteble)
            
#        cur.execute('drop table if exists message')
#        cur.execute(sql4)
        cur.execute('select * from message where id =1 or toid=1')
#        cur.executemany(sql3, param)
        data = cur.fetchall()
        for i in data:
            if i[2]==0:                
                if i[1]==1:
                    print 'receive:'+str(i)
                if i[0]==1:
                    
                    print "send:"+str(i)
            else:
                if i[1]==1:
                    print 'qunreceive:'+str(i)
                if i[0]==1:
                    
                    print "qunsend:"+str(i)


        cur.close()
        conn.commit()
        conn.close()
    except:
        conn.rollback()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])