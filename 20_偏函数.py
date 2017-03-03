#!/usr/bin/env python3
#coding:utf-8


#偏函数：通过设定参数的默认值，降低函数调用难度
#字符串转成整数
result = int('123')
print(result)#123
#指定是什么类型的进制转换
result = int('12345',base=8)
print(result)#5349
result = int('12345',base=16)
print(result)#74565

#functools.partial帮助创建偏函数，创建出转换二进制的方式
import functools
int2 = functools.partial(int,base=2)
result = int2('1111111')
print(result)#127

#partial把函数某些参数给固定住，返回新的函数，调用该函数会更简单
#调用时，是可以传入其它值的，相当于修改了默认参数的值
result = int2('111',base=16)
print(result)#273


