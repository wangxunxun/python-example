#coding=utf-8
'''
Created on 2015年3月4日

@author: xun
'''
import json
obj={"id":4,"send":'wangxun'}
test= json.dumps(obj)
print(test)
print type(test)
decodejson = json.loads(test)
print(decodejson)
print(type(decodejson))
print(decodejson['id'])

