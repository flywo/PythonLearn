#!/usr/bin/env python3
#coding:utf-8

#map()：内建函数，接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列中每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x
arr = map(f,range(10))
print(arr)#<map object at 0x101b797b8>
arr = list(arr)#因为返回的是一个Iterator惰性序列，通过list()函数把整个序列计算出来返回list
print(arr)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#把list所有数字转成字符串
arr = list(map(str,[1,2,3,4,5,6]))
print(arr)#['1', '2', '3', '4', '5', '6']


#reduce()：把一个函数作用在一个序列上，这个函数要两个参数，函数把结果和序列的下一个元素作积累计算
#比如序列求和
from functools import reduce
def add(x,y):
    return x+y
arr = reduce(add,[1,2,3,4,5])
print(arr)#15

#把序列数值换算成整数
def fn(x,y):
    return x*10+y
arr = reduce(fn,[1,2,3,4,5])
print(arr)#

#将字符串中数字转换为int
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('123'))#123

#将不规范输入英文名，变为首字母大写，其余小写
def normalize(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)#['Adam', 'Lisa', 'Bart']

#接受list并利用reduce()求积
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*9=',prod([3,5,9]))#3*5*9= 135

#把字符串123.456转换成123.456
def str2float(s):
    return reduce(map,[eval(s)])
print("str2float(\'123.456\')=",str2float('123.456'))#str2float('123.456')= 123.456

