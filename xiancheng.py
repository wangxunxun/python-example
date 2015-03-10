
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
    
'''    
'''
import threading  
  
import time  
  
class Producer(threading.Thread):  
  
    def __init__(self, t_name):  
  
        threading.Thread.__init__(self, name=t_name)  
  
   
  
    def run(self):  
  
        global x  
  
        con.acquire()  
  
        if x > 0:  
  
            con.wait()  
  
        else:  
  
            for i in range(5):  
  
                x=x+1  
  
                print "producing..." + str(x)  
  
            con.notify()  
  
        print x  
  
        con.release()  
  
   
  
class Consumer(threading.Thread):  
  
    def __init__(self, t_name):  
  
        threading.Thread.__init__(self, name=t_name)  
  
    def run(self):  
  
        global x  
  
        con.acquire()  
  
        if x == 0:  
  
            print 'consumer wait1'  
  
            con.wait()  
  
        else:  
  
            for i in range(5):  
  
                x=x-1  
  
                print "consuming..." + str(x)  
  
            con.notify()  
  
        print x  
  
        con.release()  
  
   
  
con = threading.Condition()  
  
x=0  
  
print 'start consumer'  
  
c=Consumer('consumer')  
  
print 'start producer'  
  
p=Producer('producer')  
  
   
  
p.start()  
  
c.start()  
  
p.join()  
  
c.join()  
  
print x  
'''

import threading, time  
  
class Seeker(threading.Thread):  
    def __init__(self, cond, name):  
        super(Seeker, self).__init__()  
        self.cond = cond  
        self.name = name  
  
    def run(self):  
        self.cond.acquire()  
        print self.name + ': 我已经把眼睛蒙上了'  
  
        """ 
        notify源码解析： 
            __waiters = self.__waiters 
            waiters = __waiters[:n] # 获取等待队列中的n个等待锁 
            for waiter in waiters: 
            waiter.release() # 释放Hider的等待锁 
            try: 
                __waiters.remove(waiter) 
            except ValueError: 
                pass 
        """  
        # 释放n个waiter锁，waiter线程准备执行  
        self.cond.notify()  
  
        print('notifyed...')  
  
        # 释放condition条件锁，waiter线程Hider真正开始执行  
        self.cond.wait()  
        print('waited...')  
  
        print self.name + ': 我找到你了 ~_~'  
        self.cond.notify()  
        self.cond.release()  
  
        print self.name + ': 我赢了'  
  
class Hider(threading.Thread):  
    def __init__(self, cond, name):  
        super(Hider, self).__init__()  
        self.cond = cond  
        self.name = name  
    def run(self):  
        self.cond.acquire()  
  
        """ 
        wait()源码解析： 
            waiter = _allocate_lock() # 创建一把等待锁，加入waiters队列，等待notify唤醒 
            waiter.acquire() # 获取锁 
            self.__waiters.append(waiter) 
            saved_state = self._release_save() # 释放condition.lock全局条件锁，以便其他等待线程执行 
            if timeout is None: 
                waiter.acquire() # 再次获取锁，因为已经锁定无法继续，等待notify执行release 
        """  
        # wait()释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。  
        self.cond.wait()  
  
        print self.name + ': 我已经藏好了，你快来找我吧'  
        self.cond.notify()  
        self.cond.wait()  
        self.cond.release()  
        print self.name + ': 被你找到了，哎~~~'  
  
cond = threading.Condition()  
  
hider = Hider(cond, 'hider')  
seeker = Seeker(cond, 'seeker')  
hider.start()  
seeker.start()  
  
hider.join()  
seeker.join()  
print('end...')  