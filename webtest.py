#coding=utf-8
from bottle import get, post, request ,run,route,static_file,error,response,template,os# or route
import MySQLdb
from _mysql import result

@get('/login') # or @route('/login')
def login():
    return ''' <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <br/><input value="Login" type="submit" /><input value="Register" type="button" onclick="javascrtpt:window.location.href='/register'"/>
           <div id="login_error" ></div>
        </form>'''

@post('/login') # or @route(’/login’, method=’POST’)
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')    
    if not username:
        return errormessage_login('please input username')
    elif not password:
        return errormessage_login('please input password')
    elif username and password:
        response.set_cookie("account", username, secret='some-secret-key')

        if verifyuser(username,password):
            result=searchalluser()
            print result
            return template('''<body><p>Welcome {{name}}! You are now logged in.<div id='getuser'><input type='button' value='getuser' onclick="myFunction()"/></p>
                <div id = 'demo'></div></body>
                
            <table id= "hehe" border="1" style="display:none">
            <tr>
            <th>username</th>
            <th>nickname</th>
            <th>mail</th>
            <th>datatime</th>
            <th>caozuo</th>
            </tr>
            
            %for ll in result:
                
              <tr>
              %i=0
                %while i<5:
                    %if i !=1:
                    <td>{{ ll[i] }}</td>
                  %end
                  %i =i+1
                  %end
                    <td><input type="button" name="chat" value="chat"></td>
                    %end
                    
                %end
              </tr>
            
            %end
            %end
            </table>   
                            
                            
            <script>
                function myFunction()
                {                
                if (document.getElementById("hehe").style.display=='none')
                {document.getElementById("hehe").style.display="block";
                }
                else
                {document.getElementById("hehe").style.display="none";
                }                
                }                                        
                </script>              
            
            ''', name=username,result=result)
        else:
            return errormessage_login('invaild username or password')
      


        

@get('/register')
def register():
    return '''<form method="post"  action="/register">
        <div class="input_list">username:<input type="text" name="username" />
        <div class="input_list">password:<input type="password" name="password" />
        <div class="input_list">comfirmpassword:<input type="password" name="confirmpassword" />
        <div class="input_list">nickname:<input type="text" name="nickname" />
        <div class="input_list">mail:<input type="text" name="mail" />
        <div class="submit"><input type="submit" value="submit" /><input type="button" value="back" onclick="javascrtpt:window.location.href='/login'"/>
        <div id="register_error1" ></div>
        </form>'''
    
@post('/register')
def do_register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    comfirmpassword = request.forms.get('confirmpassword')
    nickname = request.forms.get('nickname')
    mail = request.forms.get('mail')
    if not username:
        print errormessage_register('please input username')
        return errormessage_register('please input username')
    elif not password:
        return errormessage_register('please input password')
    elif not comfirmpassword:
        return errormessage_register('please input comfirmpassword')
    elif password!=comfirmpassword:
        return errormessage_register('the password is not the same')
    elif saveuser(username, password,comfirmpassword, nickname, mail)==0:        
        return errormessage_register('the username has been registered')
    else:
        return errormessage_register('success')

def mysqlconnect():
    return MySQLdb.connect(host='69.164.202.55',user='test',passwd='test',db='test',port=3306)
    


def errormessage_login(message):
    return template( ''' <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <br/><input value="Login" type="submit" /><input value="Register" type="button" onclick="javascrtpt:window.location.href='/register'"/>
           <div id="login_error" >{{errormessage}}</div>
            </form>''',errormessage=message)     
    
def errormessage_register(message):
    return template('''<form method="post"  action="/register">
    <div class="input_list">username:<input type="text" name="username" />
    <div class="input_list">password:<input type="password" name="password" />
    <div class="input_list">comfirmpassword:<input type="password" name="confirmpassword" />
    <div class="input_list">nickname:<input type="text" name="nickname" />
    <div class="input_list">mail:<input type="text" name="mail" />
    <div class="submit"><input type="submit" value="submit" /><input type="button" value="back" onclick="javascrtpt:window.location.href='/login'"/>
    <div id="register_error1" >{{errormessage1}}</div>
    </form>''',errormessage1=message)
            
            
    
def verifyuser(username,password):
    conn=mysqlconnect()
    cur=conn.cursor()
    cur.execute("select * from users where username='%s' and password='%s'"%(username,password))  
    result = cur.fetchall()
    return result

def searchalluser():
    conn=mysqlconnect()
    cur=conn.cursor()
    cur.execute("select * from users")
    result = cur.fetchall()
    print result
    print len(result)
    return result
    



def saveuser(username,password,comfirmpassword,nickname,mail): 
    createtableusers = """CREATE TABLE users (
     username  CHAR(20) not null,
     password CHAR(20) not null,
     nickname char(20),
     mail char(60),
     dt timestamp not null default now(),
     primary key(username)
     )"""        

    conn=mysqlconnect()
    cur=conn.cursor()
    if cur.execute('show tables like "users"') == 0:
        cur.execute(createtableusers)
#            cur.execute('drop table if exists message')
    try:
#            cur.execute(self.createteble)
        cur.execute(("select * from users where username = '%s'") % username)
        result = cur.fetchall()
        if result:
            return 0
            print('username is dumplicate')
        else:

            cur.execute("INSERT INTO users(username, \
       password,nickname,mail) \
       VALUES ('%s', '%s','%s','%s')" % \
       (username,password,nickname,mail))
            result = cur.fetchall()
            print(result)
            cur.close()
            conn.commit()
            conn.close()
            return 1
    except:
        conn.rollback()
        


run(host='localhost', port=8080)
