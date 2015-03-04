#coding=utf-8
from bottle import get, post, request ,run,route,static_file,error,response,template,os# or route
import MySQLdb




@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" /><input value="Register" type="button" />
        </form>
    '''
@post('/login') # or @route(’/login’, method=’POST’)
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username and password:
        response.set_cookie("account", username, secret='some-secret-key')
        if verifyuser(username,password):
            return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
        else:
            return "<p>Login failed.</p>"
    
def verifyuser(username,password):
    conn=MySQLdb.connect(host='69.164.202.55',user='test',passwd='test',db='test',port=3306)
    cur=conn.cursor()
    cur.execute("select * from users where username='%s' and password='%s'"%(username,password))  
    result = cur.fetchall()
    print(result)
    return result

def savesql():
    username = 'wangxun'
    password = "123456"
    createteble = """CREATE TABLE users (
     username  CHAR(20),
     password CHAR(20)
     )"""     
     
    conn=MySQLdb.connect(host='69.1624.202.55',user='test',passwd='test',db='test',port=3306)
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
    


run(host='localhost', port=8080)
