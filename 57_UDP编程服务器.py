#/usr/bin/env python3
#coding:utf-8


import socket
#DGRAM指定这个socket是UDP，不需要调用listen()方法
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#端口绑定
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('127.0.0.1', 9999))
print('绑定到9999')
while True:
    #recvfrom返回数据和客户端的地址与端口
    data, addr = s.recvfrom(1024)
    print('接收到：%s:%s' % addr)
    #sendto()把数据用UDP发送给客户端
    s.sendto(b'Hello, %s!' % data, addr)



