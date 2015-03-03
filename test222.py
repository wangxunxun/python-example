#coding=utf-8
'''
Created on 2015年2月28日

@author: xun
'''
import MySQLdb
def savesql():
    username1 = 'wangxun2'
    password1 = "123456"
    nickname1 = "hello"
    mail1 = "59853844@qq.com"
    send1 ='wangxun'
    receive1 = 'wangxun2'
    message1 = '34343434354523223454'
    
    
    
    createtableusers = """CREATE TABLE users (
     username  CHAR(20) not null,
     password CHAR(20) not null,
     nickname char(20),
     mail char(60),
     primary key(username)
     )"""     
    
    createtablemessage = """CREATE TABLE message (
    qunid int(11) default '0',
    send  CHAR(20) not null,
    receive CHAR(20) not null,
    message char(60),
    dt timestamp not null default now()
    
    )"""    
     
    conn=MySQLdb.connect(host='69.164.202.55',user='test',passwd='test',db='test',port=3306)
    cur=conn.cursor()

    if cur.execute('show tables like "users"') == 0:

        cur.execute(createtableusers)
    if cur.execute('show tables like "message"') == 0:

        cur.execute(createtablemessage)        
        
        
#            cur.execute('drop table if exists message')
    try:
#            cur.execute(self.createteble)

#        cur.execute("INSERT INTO users (username,password,nickname,mail) VALUES('%s','%s','%s','%s')" %(username1,password1,nickname1,mail1))
#        print(cur.fetchall())        
#        cur.execute("INSERT INTO message (send,receive,message) VALUES('%s','%s','%s')" %(send1,receive1,message1))
        cur.execute("select * from message where dt between '2015-03-03 11:14:05' and '2015-03-03 11:19:00'")
        print(cur.fetchall())   
        cur.close()
        conn.commit()
        conn.close() 
    except:
#        cur.execute("drop table if exists users1")
#        cur.execute("drop table if exists message")

        conn.rollback()

savesql()

