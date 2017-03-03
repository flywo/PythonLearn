#!/usr/bin/env python3
#coding:utf-8

#迭代器：可以用for循环遍历的数据类型有：list,tuple,dict,set,str等
#还有generator,包括生成器和待yield的函数，可以用作for循环的对象统称可迭代对象Iterable
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))#True
print(isinstance(100,Iterable))#False

#判断一个对象是否是迭代器Iterator
print(isinstance((x*x for x in range(10)),Iterator))#True
print(isinstance([],Iterator))#False

#生成器都是迭代器，虽然list等是可以迭代的，但不是迭代器
#使用iter()可以把list等可迭代对象变成迭代器
print(isinstance(iter([]),Iterator))#True
print(isinstance(iter('abc'),Iterator))#True

#凡是可以作用于for循环的对象都是Iterable类型
#凡是可以作用于next()函数的对象都是Iterator类型，表示一个惰性计算序列
#list/dict/str等式Iterable类型，但不是Iterator类型，可以通过iter()函数获得Iterator对象
