#!/usr/bin/env python3
#coding:utf-8

#StringIO:在内存中读写的str
from io import StringIO
f = StringIO()
print(f.write("Hello"))#5
print(f.write(' '))#1
print(f.write('world!'))#6
print(f.getvalue())#Hello world!
#getvalue()用于获取写入后的str


#读取StringIO，可以像读取文件一样
f = StringIO('Hello')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())#Hello


#BytesIO:如果要操作内存中的二进制数据，就需要使用BytesIO
#实现了在内存中读写bytes，创建一个BytesIO，然后写入一些bytes
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))#6
print(f.getvalue())#b'\xe4\xb8\xad\xe6\x96\x87'
#写入的不是str，而是utf-8编码的bytes


#初始化BytesIO,就像读文件一样
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())#b'\xe4\xb8\xad\xe6\x96\x87'

