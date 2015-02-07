Str1 = 'nickname:888%uniquecode123%,sendtime:2015-02-07 13:12:50%uniquecode123%,message:6666'
Str2 = '%uniquecode123%,'
nickname=Str1[9:Str1.find(Str2)]
print nickname
a=Str1[Str1.find(Str2)+16:]

sendtime = a[9:a.find(Str2)]
print sendtime
b = a[a.find(Str2)+16:]

message = b[8:]
print message

data={}
data['nickname']=nickname
data['sendtime']=sendtime
print data

