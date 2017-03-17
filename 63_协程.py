#/usr/bin/env python3
#coding:utf-8


#执行过程中，子程序内部可以中断，转而执行别的子程序，在适当的时候在返回接着执行
def a():
    print('1')
    print('2')
    print('3')
def b():
    print('x')
    print('y')
    print('z')
#generator实现协程
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 ok'
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
c = consumer()
produce(c)