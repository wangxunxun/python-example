#coding=utf-8
from bottle import get, post, request ,run,route,static_file,error,response,template,os# or route





@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
@post('/login') # or @route(’/login’, method=’POST’)
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username and password:
        response.set_cookie("account", username, secret='some-secret-key')
        return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    else:
        return "<p>Login failed.</p>"
    
@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."
    
@get('/upload') # or @route('/upload')
def upload():   
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            Category: <input type="text" name="category" />
            Select a file: <input type="file" name="upload" />
            <input type="submit" value="Start upload" />
        </form>
    '''
@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    print name,ext
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'
    save_path = 'C:/Users/xun/Pictures'
    try:
        upload.save(save_path) # appends upload.filename automatically
        return 'OK'    
    except:
        return 'File exists.'
    
    
    
    
'''    
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='C:/Users/xun/Pictures')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='C:/Users/xun/Pictures')
'''
@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='C:/Users/xun/Pictures', download=filename)

@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"



run(host='localhost', port=8080)
