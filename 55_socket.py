#/usr/bin/env python3
#coding:utf-8


#创建基于TCP的socket
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
#AF_INET指的是IPV4协议，AF_INET6指的是IPV6协议。SOCK_STREAM:面向流的TCP协议
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)
s.close()
#recv(max)接收数据，一次性接收指定的字节数，在一个while循环中反复接收，知道recv()返回空数据
#完毕后调用close()方法关闭socket，一次完整通信就结束了。
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
