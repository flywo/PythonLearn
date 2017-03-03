#!/usr/bin/env python3
#coding:utf-8


'''
迭代：通过for循环遍历list或tuple等可迭代对象，就称为迭代
'''
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)#b c a

#默认情况下，dict迭代的是key，如果要迭代value，需要如下：
for value in d.values():
    print(value)#2 1 3

#同时迭代key和value
for k,v in d.items():
    print(k,v)#a 1 c 3 b 2

#字符串也可以迭代
for ch in 'abcd':
    print(ch)#a b c d

#判断对象是否可迭代，通过collections模块的iterable类型判断
from collections import Iterable
print(isinstance('abcd',Iterable))#True
print(isinstance(111,Iterable))#False

#同时遍历list中的索引-元素
for i,value in enumerate([1,2,3,4,5]):
    print(i,value)


#同时使用两个变量
for x,y in [(1,2),(2,4)]:
    print(x,y)