#coding=utf-8
'''
Created on 2015年2月28日

@author: xun
'''
import MySQLdb
def savesql():
    username = 'wangxun'
    password = "123456"
    createteble = """CREATE TABLE users (
     username  CHAR(20),
     password CHAR(20)
     )"""     
     
    conn=MySQLdb.connect(host='69.164.202.55',user='test',passwd='test',db='test',port=3306)
    cur=conn.cursor()
    if cur.execute('show tables like "users"') == 0:
        cur.execute(createteble)
#            cur.execute('drop table if exists message')
    try:
#            cur.execute(self.createteble)

        cur.execute("INSERT INTO users(username, \
   password) \
   VALUES ('%s, '%s')" % \
   (username,password))

        cur.close()
        conn.commit()
        conn.close()
    except:
        conn.rollback()

savesql()