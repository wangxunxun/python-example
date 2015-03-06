#coding=utf-8
from bottle import get, post, request ,run,route,static_file,error,response,template,os# or route
import MySQLdb
from _mysql import result
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
                <script>
                    function myFunction()
                    {
          var mybody = document.getElementsByTagName("body")[0]; 
           mytable = document.createElement("table"); 
        mytablebody = document.createElement("tbody"); 
        
             
        mytabletr = document.createElement("tr");
        mycell=  document.createElement("th"); 
        username = document.createTextNode("username");
         mycell.appendChild(username);       
        mytabletr.appendChild(mycell);
        
      
        
        mycell=  document.createElement("th"); 
        username = document.createTextNode("nickname");
         mycell.appendChild(username);       
        mytabletr.appendChild(mycell);
        
               mycell=  document.createElement("th"); 
        username = document.createTextNode("mail");
         mycell.appendChild(username);       
        mytabletr.appendChild(mycell); 
        
                mycell=  document.createElement("th"); 
        username = document.createTextNode("datatime");
         mycell.appendChild(username);       
        mytabletr.appendChild(mycell);
        
                mycell=  document.createElement("th"); 
        username = document.createTextNode("caozuo");
         mycell.appendChild(username);       
        mytabletr.appendChild(mycell);
        
        
        
        mytablebody.appendChild(mytabletr); 
mytable.appendChild(mytablebody); 
//将<table>添加到<body> 
mybody.appendChild(mytable);     
    
       
        
        
         for(var j = 0; j < 5; j++) { 
// 创建一个<tr>元素 
mycurrent_row = document.createElement("tr"); 
for(var i = 0; i < 5; i++) { 
// 创建一个<td>元素 
mycurrent_cell = document.createElement("td"); 
//创建一个文本节点 
currenttext = document.createTextNode({{for i in result }}); 
// 将创建的文本节点添加到<td>里 
mycurrent_cell.appendChild(currenttext); 
// 将列<td>添加到行<tr> 
mycurrent_row.appendChild(mycurrent_cell); 
} 
// 将行<tr>添加到<tbody> 
mytablebody.appendChild(mycurrent_row); 
} 
// 将<tbody>添加到<table> 
mytable.appendChild(mytablebody); 
//将<table>添加到<body> 
mybody.appendChild(mytable); 
// 将表格mytable的border属性设置为2 
mytable.setAttribute("border", "2"); 
}        
                                
                </script>             
            
            ''', name=username,result=result)
        else:
            return errormessage_login('invaild username or password')