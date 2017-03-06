#!/usr/bin/env python3
#coding:utf-8


#定制类：class中有许多特殊的函数，帮助我们定制类
#__str__:类、实例信息打印
class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('Bobo'))#<__main__.Student object at 0x101279780>

#使用__str__()方法，返回自定义的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Bobo'))#Student object (name: Bobo)

#__repr__()，调试返回的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__= __str__
print(Student('Bobo'))#


#__iter__:如果一个类想被用于for...in循环，就必须实现__iter__()方法，该方法返回一个
#迭代对象，for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，知道遇到
#StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self#实例本身就是迭代对象，返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b#计算下一个值
        if self.a > 100:#退出循环条件
            raise StopIteration()
        return self.a#返回下一个值
for n in Fib():
    print(n)


#__getitem__：将上方的Fib按照list那样通过下标取元素
class Fib(object):
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a,b = b, a+b
        return a
f = Fib()
print(f[4])#5
#支持切片，切片对象slice
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(n):
              a, b = b, a+b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
f = Fib()
print(f[:5])#[1, 1, 2, 3, 5]
print(f[4:10])#[5, 8, 13, 21, 34, 55]


#__getattr__:获得类方法或属性
class Student(object):
    def __init__(self):
        self.name = 'Mic'
#此时如果调用了一个没有的属性，会报错，此时可以写一个__getattr__()方法，动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Mic'
    def __getattr__(self, item):
        if item == 'score':
            return 99
s = Student()
print(s.score)#99
#当不存在属性时，python解释器会视图调用__gettattr__(self,'score')来获得属性

#返回函数：
class Student(object):
    def __getattr__(self, item):
        if item == 'age':
            return lambda: 25
s = Student()
fn = s.age
print(fn())#25
#只有在没有找到属性的情况下，才会调用__getattr__，已有的不会查找

#让class只特定的响应几个属性的默认返回，就需要抛出错误
class Student(object):
    def __getattr__(self, item):
        if item == 'age':
            return lambda : 30
        raise AttributeError('没有该属性:%s' % item)
s = Student()
print(s.age)
# print(s.name) #报错

#利用__getattr__链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list)#/status/user/timeline/list


#__call__:对象实例调用方法时，实际上是用instance.method()来调用的,定义一个__call__()方法，实现直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)
s = Student('Mic')
s()#My name is Mic

#__call__还可以定义参数，对实例进行直接调用就好比对一个函数进行调用
#如果一个对象能够被调用，则就是一个Callable对象
print(callable(s))#True
print(callable(max))#True
#可以通过callable()函数判断一个对象是否是可调用对象
