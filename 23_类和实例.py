#!/usr/bin/env python3
#coding:utf-8

#类：通过关键字class定义，后面紧跟类名，通常是大写开头，紧接着(object)表示该类从哪个类继承下来的，如果没有合适的，就使用object
class Student(object):
    pass

#实例化
bart = Student()
print(bart)#<__main__.Student object at 0x101a797b8>
print(Student)#<class '__main__.Student'>

#可以自由的给实例变量绑定属性
bart.name = 'Angle'
print(bart.name)#Angle

#可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去，通过定义一个特殊的__init__方法，在创建实例的时候，把name，score等属性绑定上去
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
#__init__方法第一个参数永远是self,表示创建实例本身，有了__init__方法，在创建实例的时候，就不能传入空的参数了
bart = Student("BOBO",90)
print(bart.name)#BOBO
print(bart.score)#90

#和普通函数相比，定义函数第一个参数永远是self，并且，不需要传入该值，别的和普通函数没有区别

#定义方法：类里面的方法，第一个参数是self，其余的和普通函数是一样的
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' % (self.name, self.score))
bart = Student('Angle', 90)
bart.print_score()#Angle : 90

