#/usr/bin/env python3
#coding:utf-8


#多进程：fork()函数调用一次，返回两次，操作系统自动把当前进程复制一份，然后
#分别在父进程和子进程返回，子进程返回0，父进程返回子进程ID，父进程可以fork出多个
#子进程，所以父进程要记下每个子进程ID，而子进程只需要调用getppid()拿到父进程ID

#fork创建出子进程
import os
# print('子进程开启：%s' % os.getpid())
# #2577
# pid = os.fork()
# if pid == 0:
#     print('子进程：%s,父进程：%s' % (os.getpid(),os.getppid()))
# else:
#     print("我是父进程：%s，创建出子进程：%s" % (os.getpid(),pid))

#fork函数，在接到新的任务时，就可以复制出一个子进程来处理新的任务
#apache服务器就是由父进程监听端口，有新的http请求时，fork出子进程来处理http请求


#multiprocessing:款平台的多进程模块
#process类表示一个进程对象
from multiprocessing import Process
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))
if __name__ =='__main__':
    print('父进程：%s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程开始')
    p.start()
    p.join()
    print('子进程结束')
'''
父进程：2771
子进程开始
Run child process test (2772)
子进程结束
'''

#创建子进程时，只需要传入一个执行函数和函数参数，创建出process实例，用start启动，
# join方法等待子进程结束后继续执行


#pool：如果需要大量子进程，可以用进程池的方式批量创建
from multiprocessing import Pool
import time, random
def long_time_task(name):
    print('运行工作：%s'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('任务%s执行了%s秒'%(name,(end-start)))
if __name__=="__main__":
    print('父进程：%s'%os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("等所有进程执行完毕")
    p.close()
    p.join()
    print("执行完毕")

