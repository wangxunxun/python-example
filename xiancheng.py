
#coding=utf-8
'''
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(4):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))

threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    sleep(15)
    print(ctime())
    print '333'
    print t1.is_alive()
    print t2.is_alive()
    

    print "all over %s" %ctime()
    
'''    
'''
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(5):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
#子线程未执行完前，主线程阻塞
    t.join()
    sleep(15)
    print(ctime())
    print '333'
    print t1.is_alive()
    print t2.is_alive()
    print "all over %s" %ctime()
'''   
''' 
import time  
import thread  
def timer(no, interval):  
    cnt = 0  
    while cnt<10:  
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        cnt+=1  
#    thread.exit_thread()  
     
   
def test(): #Use thread.start_new_thread() to create 2 new threads  
    thread.start_new_thread(timer, (1,1))  
    thread.start_new_thread(timer, (2,2))  
   
if __name__=='__main__':  
    test()  
    
'''    
    
import threading  
import time  
class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:  
            print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())  
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         
   
def test():  
    thread1 = timer(1, 1)  
    thread2 = timer(2, 2)  
    thread1.start()  
    thread2.start()  
    time.sleep(10)  
    thread1.stop()  
    thread2.stop()  

    return  
   
if __name__ == '__main__':  
    test()  