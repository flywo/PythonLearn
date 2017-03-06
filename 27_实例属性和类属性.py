#!/usr/bin/env python3
#coding:utf-8


#python根据类创建的实例可以任意绑定属性
class Studen(object):
    def __init__(self, name):
        self.name = name
s = Studen('Angle')
s.score = 90

#类属性，如下，定义后，所有实例都可以访问
class Studen(object):
    name = 'Student'
s = Studen()
print(s.name)#Studnet，s并没有name属性，所以会继续查找class的name属性
print(Studen.name)#Student
s.name = 'BOBO'#相当于给s绑定了name属性
print(s.name)#BOBO
print(Studen.name)#Student
Studen.name = 'BOBO'
print(Studen.name)#BOBO
Studen.name = 'Angle'
del s.name#属性name被删除
print(s.name)#Angle，重新读取class的name属性

#所以千万不要把实例属性和类属性使用相同的名字，相同名字的实例属性将屏蔽掉类属性，但是删除实例属性后，再使用，将访问到类属性
