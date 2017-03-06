#!/usr/bin/env python3
#coding:utf-8


#判断对象类型
print(type(123))#<class 'int'>
print(type('123'))#<class 'str'>
print(type(abs))#<class 'builtin_function_or_method'>

#type()返回的是class类型，可以比较两个变量的type类型是否相同
print(type(123)==type(234))#True
print(type(123)==type('123'))#False

#基本数据类型可以通过int,str判断
print(type(123)==int)#True
print(type('123')==str)#True

#判断对象是否是函数
import types
def fn():
    pass
print(type(fn)==types.FunctionType)#True
print(abs==types.BuiltinFunctionType)#False

#使用isinstance()判断
print(isinstance(123,int))#True

#判断变量是否是某些类型中的一种，比如判断是否是list或者tuple
print(isinstance([1,2,3],(list, tuple)))#True
print(isinstance((1,2,3),(list, tuple)))#True


#使用dir():获得一个对象的所有属性和方法，使用dir()函数，返回一个包含字符串的list
print(dir('abc'))#['__add__', '__class__', '__contains__',
# '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getnewargs__', '__gt__', '__hash__', '__init__',
# '__iter__', '__le__', '__len__', '__lt__', '__mod__',
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', 'capitalize', 'casefold',
# 'center', 'count', 'encode', 'endswith', 'expandtabs',
#  'find', 'format', 'format_map', 'index', 'isalnum',
# 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
#  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']

#len()函数，获取一个对象的长度，在len()函数内部，会自动调用__len__()方法，所以下面代码是等价的
print(len('abc'))#3
print('abc'.__len__())#3

#如果我们自己写的类也想用len(obj)的话，就需要自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))#100

#配合getatter()、setattr()、hasattr()可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x
obj = MyObject()
print(hasattr(obj,'x'))#是否有属性x:true
print(hasattr(obj,'y'))#false
setattr(obj,'y',19)#设置一个属性y为19
print(obj.y)#19
print(getattr(obj,'y'))#获得一个属性y，值为19

#可以传入一个默认参数，如果属性不存在就返回默认值
print(getattr(obj,'z',404))#404

#获得对象的方法
print(hasattr(obj,'power'))#true

#获取属性power
fn = getattr(obj,'power')
print(fn())#81

#如果知道对象内部信息时，不需要使用getattr去获取对象信息，应该直接使用
def readImage(fp):
    if hasattr(fp,'read'):
        #如果fp有read方法
        return fp.read()
    return None


