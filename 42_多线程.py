#/usr/bin/env python3
#coding:utf-8


#多线程：Python的线程是真正的posix thread，而不是模拟出来的线程
#_thread:低级模块  threading:高级模块，对低级模块进行了封装
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading
#新线程执行的代码
def loop():
    print('线程：%s 正在运行' % threading.current_thread().name)
    n = 0
    while n < 5:
        n+=1
        print('线程：%s --> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('线程：%s 结束' % threading.current_thread().name)
print('线程%s 正在运行中' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('线程:%s 结束' % threading.current_thread().name)
'''
任何进程会启动一个主线程，主线程可以启动新的线程。threading模块有个current_thread()函数
永远返回当前线程的实例，主线程实例名字叫MainThread，子线程的名字在创建时指定，名字仅仅在
打印时显示用，没有别的意义
'''

#Lock：多进程中，同一个变量，有各自的拷贝存在每一个进程中，互不影响，而多线程中，所有
#变量都由所有线程共享，任何一个变量可以被任何一个线程修改。这时，我们就需要加锁，防止出现这种情况
'''
创建锁：threading.Lock()
获取锁：lock.acquire()
释放锁：lock.release()
'''

#多核CPU：由于解释器设计问题，ptyhon中，使用多线程，不要指望能有效利用多核，都是用的1个核

