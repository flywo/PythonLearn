#/usr/bin/env python3
#coding:utf-8


#python内置了一个WSGI服务器
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
#启动服务器
from wsgiref.simple_server import make_server
#创建服务器，ip地址为空，端口是8000，处理函数是application
httpd = make_server('', 8000, application)
print('服务器端口打开了...')
#监听http请求
httpd.serve_forever()
#就可以在浏览器输入http://localhost:8000/得到结果
#入口都是WSGI处理函数，http请求的所有输入信息都可以通过environ获得，http响应的输出都可以通过start_response()加上函数返回值作为body

