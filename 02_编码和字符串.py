#!/usr/bin/env python3
#coding:utf-8

#Unicode编码：把所有语言统一到一套编码里
#UTF-8编码：可变长的Unicode编码，合理利用空间
#ASCII编码实际上是UTF-8编码的一部分
#计算机内存中，统一使用Unicode编码，保存到硬盘或需要传输时，转成UTF-8编码。
#所以，从文件中读取UTF-8字符会被转成Unicode字符到内存中，编辑完成后，又转成UTF-8保存到文件。
#浏览网页时，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器。

#字符串，Python3中，字符串是用的Unicode编码，所以Python字符串是支持多语言的。
print('包含中文的String')#包含中文的String

#ord()：获取单个字符的整数表示   chr()：把编码转换成对应的字符
print(ord('编'))#32534
print(chr(32534))#编

#字符串整数编码
print('\u4e2d\u6587')#中文

#字节：Python字符串类型是str，一个字符对应若干个字节，如果需要保存或传输，需要变成字节为单位的bytes
a = b'abc'#bytes类型数据，用b前缀的单引号或双引号表示

#encode()：str编码成指定的bytes
print('abc'.encode('utf-8'))#b'abc'
print('abc'.encode('ascii'))#b'abc'
print('中'.encode('utf-8'))#b'\xe4\xb8\xad'

#decode()：将bytes转成str
print(b'abc'.decode('ascii'))#abc
print(b'\xe4\xb8\xad'.decode('utf-8'))#中

#len()：计算str中包含多少个字符
print(len('abcd'))#4
print(len('中国'))#2
#如果str换成bytes，则计算字节数
print(len(b'abc'))#3
print(len(b'\xe4\xb8\xad'))#3

#格式化输出字符串
#%格式化输出
print('你好，%s，你话费快没有了，快去充话费啊！' % '大王')#你好，大王，你话费快没有了，快去充话费啊！
print('你还，%s，你还有%d块钱了，快去充话费啊！' % ('大王',10))#你还，大王，你还有10块钱了，快去充话费啊！
#%：格式化字符串，字符串中有多少个占位符，后面就需要多少个变量，只有一个，可以忽略括号
'''
%d:整数替换
%f:浮点数
%x:十六进制数
'''

'''
%2d:整数位数  %02d:整数位数，不足补0
%.2f:2位小数
'''
print('%2d-%02d' % (333,1))#333-01
print('%.2f-%03d' % (3.3333,3))#03-003

#%s:字符串替换，会把任意类型数据转换成字符串，通用
print('age:%s,name:%s' % (13,'Ha'))#age:13,name:Ha

#%%：表示一个%字符
print('100 %d %%' % 4)#100 4 %




