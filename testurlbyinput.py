#-*- coding: utf-8 -*-
import httplib2,time
import requests

def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim

class testurlbyinput:

    
    def GetHttpStatus(self):
        try:
            res = requests.get(self.url,timeout=1)
            return str(res.status_code)   
        except:
            return '504'
        
        
    def GetHttpTime(self):    
        try:
            Start=time.time()    
            requests.get(self.url,timeout=1)
            End=time.time()
            diff= End-Start
            return str(diff)
        except:
            End=time.time()
            diff= End-Start
            return str(diff)
        
    def requesturl(self):
    

        if self.GetHttpStatus() !="200":
            f2=open("C:/Users/wangxun/Documents/urlhttps-result.txt","a")
            f2.write("测试日期："+Time()+",url:"+self.url+"\n")
            f2.write( "测试结果：请求失败，错误代码为："+self.GetHttpStatus())
            f2.write('，请求持续时间：'+self.GetHttpTime())
            f2.write("\n")
            f2.close()
            print "请求失败"
        else:
            f2=open("C:/Users/wangxun/Documents/urlhttps-result.txt","a")
            f2.write("测试日期："+Time()+",url:"+self.url+"\n")
            f2.write( "测试结果：请求成功，代码为"+self.GetHttpStatus())
            f2.write('，请求持续时间：'+self.GetHttpTime())
            f2.write("\n")
            f2.close()
            print '请求成功'
            
            
        
    def run(self):
        while True:
            self.url = raw_input("raw_input: ")
            self.requesturl()

if __name__ == "__main__":  
    print "test begin: "+Time()

    test = testurlbyinput()
    test.run()
    print "test over: "+Time()
