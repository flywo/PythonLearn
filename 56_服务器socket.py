#/usr/bin/env python3
#coding:utf-8


#服务器需要监听一个端口，有客户端要连接，就建立socket连接
import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#1表示，SO_REUSEADDR为TRUE，操作系统会在服务器socket被关闭后立马释放该端口
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#127.0.0.1特殊IP地质，表示本机
s.bind(('127.0.0.1', 9999))
s.listen(5)#等待连接的最大数
print('快来连接吧')
#通过一个永久的循环接收来自客户端的连接,accept会等待并返回一个客户端的连接
def tcplink(sock, addr):
    print('新的连接来自：%s:%s' % addr)
    sock.send(b'Welcom!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('连接断开：%s:%s' % addr)
while True:
    #接受一个新的连接
    sock, addr = s.accept()
    #创建新的线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

