#!/usr/bin/env python3
#coding:utf-8


#input/output:输入和输出
#浏览器：发送数据给服务器，该动作为output，服务器返回数据浏览器接收，该动作为input
#读取磁盘：读取到内存，input操作，写入磁盘，outpu

#stream:input stream外面流入内存，output stream内存流出。

#由于cpu速度比外部速度快，操作时：
#一：cpu等着，执行完毕后再继续执行，同步IO
#二：cpu不等，去执行别的操作，异步IO

#同步与异步区别：同步，等待，异步，不等待

#同步性能低于异步，但是异步更复杂。异步需要回调模式，通知cpu任务完成，cpu还要不停轮询。


#文件读写：现代操作系统是不允许直接操作磁盘的，都是请求操作系统打开一个文件对象，
#然后通过该对象读取数据或者写入数据


#打开文件：open()函数，传入文件名和标示符
f = open('File','r')

#读取文件内容：read()函数，将文件内容读取到内存，用一个str对象表示
print(f.read())

#关闭文件：close()函数，如果使用完毕后，需要关闭文件，否则会占用操作系统资源
f.close()

#如果打开有错误，f.close()就不会回调，需要判断
try:
    f = open('s','r')
    print(f.read())
except BaseException as e:
    print('发生错误：',e)
finally:
    if f:
        f.close()

#可以使用with语句自动调用close()方法
with open('File', 'r') as f:
    print(f.read())

#read()方法会一次性读取全部内容，如果文件太大，内存会不够，需要反复调用read(size)方法
#或者readline()方法每次读取一行内容，readlines()返回所有内容，并返回list
f = open('File', 'r')
for line in f.readlines():
    print(line.strip())#把末尾的\n删除掉
f.close()

#open()返回的对象，是一个file-like object，该对象不要求从特定类继承，
#只需要一个read()方法即可，还可以是内存中的字节流、网络流、自定义流等
#stringIO就是内存中的该对象，做临时缓冲用

#二进制文件：要读取二进制文件，图片视频等，需要用'rb'模式
f = open('Spaceship.png', 'rb')
print(f.read())
f.close()

#字符编码：如果读取非utf-8编码，需要传入encoding参数，比如读取gbk编码文件
try:
    f = open('s.txt','r',encoding='gbk')
    print(f.read())
except BaseException as e:
    print('发生错误：',e)
finally:
    if f:
        f.close()

#如果文本中掺杂了非法编码字符，最简单的处理方式是忽略
try:
    f = open('s.text','r',encoding='gbk',errors='ignore')
    print(f.read())
except BaseException as e:
    print('发生错误：',e)
finally:
    if f:
        f.close()

#写文件:与读文件一样，区别是，标识符为'w'或者'wb'，表示写文本或者二进制文件
f = open('File', 'w')
f.write("Hello,world!\nHello,world!\nHello,world!\nHello,world!\nHello,world!\n")
f.close()

#当需要反复写文件时，务必要调用close关闭文件，如果忘记了close后果是数据没有写入完毕
#所以，用with最好
with open('File', 'w') as f:
    f.write('Hello,world!\nHello,world!\nHello,world!\nHello,world!\n')
