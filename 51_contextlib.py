#/usr/bin/env python3
#coding:utf-8


#任何对象，只要使用了上下文管理，都可以使用with自动管理
# with open('/path/to/file', 'r') as f:
    # f.read()


#实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print("Begin")
        return self
    def __exit__(self, exc_type, exc_value, tracebace):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about %s' % self.name)
#这样，我们就可以把自己写的资源对象用于with语句
with Query('Bob') as q:
    q.query()


#@contextmanager：可以使用标准库contextlib写上面的代码
from contextlib import contextmanager
class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s' % self.name)
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('Bob') as q:
    q.query()


#特定代码执行后，指定特定代码
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)
with tag('h1'):
    print('hello')
    print('world')
'''
1.with语句首先执行yield之前的语句
2.yield调用会执行with语句内部所有的语句
3.最后执行yield之后的语句
'''


#closing:如果一个对象没有实现上下文，就不能用于with，可以使用closing()来把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


