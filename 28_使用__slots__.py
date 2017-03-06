#!/usr/bin/env python3
#coding:utf-8


#创建出class实例后，可以给该实例绑定任何属性和方法
class Student(object):
    pass
s = Student()
s.name = 'Angle'
print(s.name)#Angle

#绑定一个方法
def set_age(self, age):#定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)#给实例绑定一个方法
s.set_age(23)#调用绑定的方法
print(s.age)#23

#给某个实例绑定方法，对别的实例是不起作用的，想给所有实例绑定，则需要给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score
#绑定后，所有实例均可调用
s = Student()
s.set_score(100)
print(s.score)#100


#使用__slots__:如果我们要限制实例的睡醒，比如值允许添加指定的属性，则需要一个特殊变量__slots__
class Student(object):
    __slots__ = ('name', 'age')#用元组定义允许的属性名称
s = Student()
s.name = 'angle'
#s.score = 90#运行时，会报错
s.age = 90
print(s.name,s.age)#angle 90

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Gra(Student):
    pass
s = Gra()
s.score = 99
print(s.score)#99

#除非在子类中也定义__slots__，这样，允许定义的属性就是自身的__slots__加上父类的__slots__
class Bra(Student):
    __slots__ = ('score')
s = Bra()
s.name = 'angle'
s.age = 90
s.score = 99
#s.meth = 'a'#会报错