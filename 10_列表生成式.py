#!/usr/bin/env python3
#coding:utf-8


#列表生成式：内置的用来生成list的生成式
#生成1-10的list
arr = list(range(1,11))
print(arr)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#列表生成式
arr = [x*x for x in range(1,11)]#相当于遍历range(1,11)，每个元素*元素自己用来生成list
print(arr)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for循环后可以加上if判断，比如筛选出偶数的平方
arr = [x*x for x in range(1,11) if x % 2 == 0]#只有x是偶数时，才会使用
print(arr)#[4, 16, 36, 64, 100]

#可以使用两层循环，生成全排列
arr = [m+n for m in 'ABC' for n in 'XYZ']
print(arr)#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#列出当前目录下所有的文件和目录名
import os
arr = [d for d in os.listdir('.')]
print(arr)

#for循环可以同时使用两个或者多个变量，比如dict的items可以同时迭代key和value
arr = {'x':1,'y':2,'z':3}
arr = [k+'='+str(v) for k,v in arr.items()]
print(arr)#['y=2', 'x=1', 'z=3']

#把list中所有的字符串变成小写
arr = ['Hello','world','apple']
arr = [s.lower() for s in arr]
print(arr)#['hello', 'world', 'apple']

#过滤掉不符合的元素
arr = ['Hello','world','apple',1]
arr = [s.upper() for s in arr if isinstance(s, str)]
print(arr)#['HELLO', 'WORLD', 'APPLE']