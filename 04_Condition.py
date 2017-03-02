#!/usr/bin/env python3
#coding:utf-8


#条件判断
age = 20
if age > 18:
    print('%d岁，成年了！' % age)#20岁，成年了！

#if...else...
if age > 18:
    print('成年了')#成年了
else:
    print('未成年')

#if...elif...else...
if age < 18:
    print('未成年')
elif age > 80:
    print('你老了')
else:
    print('很年轻')#很年轻

#if简写：判断的值是非零数值，非空字符串，非空list等，就为True
if age: print('True')#True


#input:读取用户输入
age = input('输入年龄：')
#input返回的数据类型是str，需要转换
age = int(age)
if age < 18:
    print('未成年')
elif age > 80:
    print('你老了')
else:
    print('很年轻')

