#!/usr/bin/env python3
#coding:utf-8


'''
模块：一个.py文件就称为一个模块
好处：
1.提高代码可维护性
2.避免函数名和变量名冲突
'''

#模块使用：导入模块
__author__ = 'YuHua'#作者，相当于给代码签名，表示这是你写的代码
import sys#导入之后，利用sys变量访问所有功能
def test():
    args = sys.argv#python3 xxx.py获得的值是【'xxx.py'】，python3 xxx.py michale是【'xxx.py'，'michale'】
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':#如果命令行运行该文件，__name__会等于__main__，别的地方导入的该模块，则不会等于__main__
    test()

'''
作用域：有的函数和变量是希望内模块内部使用的，通过前缀_实现
1.正常函数和变量名是公开的，可以直接被引用，比如abc,x234
2.__xxx__特殊变量，可以直接引用，但是有特殊用途，比如__author__，__name__,__doc__表示注释
3._xxx和__xxx函数或变量是非公开的，不应该被直接引用，比如_abc,__abc等
'''
def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('aaaa'))#Hello, aaaa
print(greeting('aa'))#Hi, aa

