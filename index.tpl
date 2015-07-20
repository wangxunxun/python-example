
<div id='getuser'><input type='button' value='getuser' onclick="myFunction()"/>

<table id= "hehe" border="1" style="display:none">
<tr>
<th>username</th>
<th>nickname</th>
<th>mail</th>
<th>datatime</th>
<th>caozuo</th>
</tr>

%for ll in key:
    
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