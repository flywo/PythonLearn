#!/usr/bin/env python3
#coding:utf-8


#装饰器：函数是一个对象，可以被赋值给变量，可以通过变量调用该函数
def now():
    print('2017')
f = now
f()#2017

#函数对象有一个__name__属性，可以拿到函数名
print(now.__name__)#now
print(f.__name__)#now

#不希望修改now函数，又动态增加功能，则需要使用装饰器Decorator
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
#通过@语法，把装饰器置于函数定义处：
@log
def now():
    print('2017')
now()#call now() 2017
#now()函数执行时，还会有一段打印
#把@log放到now()函数定义处，相当于执行了语句：now = log(now)

#自定义装饰器输入参数
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2017')
now()
#三层嵌套效果相当于：now = log('execute')(now)

#完整的装饰器，不带参数
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(**args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

#待参数
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator



