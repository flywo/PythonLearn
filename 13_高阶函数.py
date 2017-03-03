#!/usr/bin/env python3
#coding:utf-8

#变量可以指向函数
f = abs
print(f)#<built-in function abs>
print(f(-1))#1

#函数名也是变量
#abs = 10
#print(abs(1))会报错，abs已经不再指向函数
#print(abs)#10

#如果要让修改函数名变量指向的改变，其它模块也要生效，可以这样：
#import builtins;builtins.abs = 10

#传入函数：函数的参数可以接收变量，一个函数可以接收另一个函数作为参数，这种函数称之为高阶函数
def add(x,y,f):
    return f(x)+f(y)
print(add(-9,-10,abs))#19




