#/usr/bin/env python3
#coding:utf-8


#ThreadLocal:解决参数在一个线程中各个函数之间传递的问题

'''
import threading
创建全局对象：local = threading.local()
获取当前线程关联的对象：local.student
绑定student:local.student = name
'''