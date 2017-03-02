#!/usr/bin/env python3
#coding:utf-8


#数据类型转换
print(int('123'))#123
print(int(12.34))#12
print(float('12.34'))#12.34
print(str(100))#'100'
print(bool(1))#True
print(bool(''))#False
print(hex(255))#0xff


#函数定义,如果函数执行完毕后，没有return数据，则会返回None
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-10))#10

#空函数，pass语句表示什么也不做
def nop():
    pass
if 3 > 1:
    pass

#参数检查，isinstance数据类型检查
def my(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        print('正数')
    else:
        print('负数')
# my('f')#程序执行时会报错

#多个返回值
import math
def move(x,y,setp,angle=0):
    nx = x+setp*math.cos(angle)
    ny = y-setp*math.sin(angle)
    return nx,ny
print(move(1,2,1,1))#返回了一个元组，可以省略括号


#函数参数
#位置参数：下方的x就是位置参数，调用时必须传入一个参数x
def power(x):
    return x*x
print(power(10))#100

def power(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print(power(10,3))#1000

#默认参数：给一个参数设置默认值，如果调用时没有设置，则使用默认值
#默认参数必须在位置参数后，如果不按照顺序提供默认参数，则需要把参数名写上
#默认参数必须是不可变对象
def powerf(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powerf(100))#10000

#可变参数：传入的参数是可变的
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
print(calc(1,3,5,7))#84
#传入list或者tuple
nums = [1,3,5,7]
print(calc(*nums))#84

#关键字参数：允许传入0个或任意个参数名的参数，参数在函数内部自动组装成一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('xiaoming',12,gender='M',job='engineer')#name: xiaoming age: 12 other: {'job': 'engineer', 'gender': 'M'}
#也可以传入dict
extra = {'city':'beijing','job':'engineer'}
person('xiaoming',22,**extra)#name: xiaoming age: 22 other: {'city': 'beijing', 'job': 'engineer'}

#命名关键字参数：函数调用者可以传入任意不受限制的关键字参数，在函数内部通过kw检查
def person(name,**kw):
    if 'city' in kw:
        print('有city参数')
    if 'job' in kw:
        print('有job参数')
    print('name:',name,'other:',kw)
person('xiaoming',city='beijing',addr='chaoyang')#name: xiaoming other: {'addr': 'chaoyang', 'city': 'beijing'}
#限制关键字参数的名字，就需要用命名关键字参数,命名参数必须要传入参数名
def person(name,*,city,job):
    print(name,city,job)
person('jack',city='beijing',job='en')#jack beijing en
#如果函数中有一个可变参数，则不再需要*
def person(name,*args,city,job):
    print(name,args,city,job)
person('jack',city='beijing',job='en')#jack () beijing en

#参数组合，参数定义顺序必须是：必选参数、默认参数、可变参数、命令关键字参数、关键字参数


#递归函数：自己调用自己
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))#120

#尾递归：函数返回的时候，调用自身本身，return语句不能包含表达式
def fact1(n):
    return fact_iter(n, 1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact1(5))#120

