#!/usr/bin/env python3
#coding:utf-8


#动态语言与静态语言最大区别：函数类的定义是编译时定义，而是运行时创建

#当导入一个模块时，解释器会依次执行该模块的语句，然后动态创建出一个hello的class对象
from Hello import Hello
h = Hello()
h.hello()#Hello, world.
h.hello('boy')#Hello, boy.

#type()函数查看一个类型或变量类型
print(type(h))#<class 'Hello.Hello'>
print(type(Hello))#<class 'type'>

#class是动态创建的，创建class的方法就是使用type()函数
#type()函数即可返回一个对象的类型，又可以创建出新的类型
def fn(self, name='wori'):#先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn))#创建Hello class
h = Hello()
h.hello()#Hello, wori.
h.hello('woca')#Hello, woca.

print(type(h))#<class '__main__.Hello'>
print(type(Hello))#<class 'type'>

'''
创建出一个class对象，type()函数需要依次传入3个参数
1.class名称
2.继承的父类集合，多重继承，需要传入一个tuple
3.class的方法名称与函数绑定
'''
Hello = type('Hello', (object,), dict(hello=fn))
#上方创建出的的类和直接写class是完全一样的


#metaclass：控制类的创建行为，metaclass允许创建类或者修改类。类可以看成是metaclass创建出来的实例
#metaclass给自定义的类添加一个方法
class ListMetaclass(type):#metaclass是类的模板，所以必须从type类型派生
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
#有了listmetaclass，在定义类的时候还要指示使用listmetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    pass
#传入关键字参数metaclass时，就生效了，指示解释器在创建MyList时，通过ListMetaclass.__new__()来创建
#在此，我们可以修改类的定义，比如加上新的方法，然后返回修改后的定义

#__new()__方法接收到的参数依次是：
#1.当前准备创建的类的对象
#2.类的名字
#3.类继承的父类集合
#4.类的方法集合
l = MyList()
l.add(1)
print(l)#[1]

