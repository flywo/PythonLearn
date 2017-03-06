#!/usr/bin/env python3
#coding:utf-8


#如果要让内部属性不被外部访问，可以在属性名称前加上两个下划线，这样就变成了私有变量，只能内部访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))
stu = Student('BOBO', 90)
stu.print_score()#BOBO : 90
#此时，已经无法使用stu.__name去访问变量
# print(stu.__name)会报错

#如果外部需要获取name，score，则需要增加get_name和get_score方法
#如果需要外部修改name,score，则需要增加set_name和set_score方法
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        self.__score = score
stu = Student('Angle', 99)
print(stu.get_name())#Angle
print(stu.get_score())#99
stu.set_name('Baby')
stu.set_score(98)
print(stu.get_name())#Baby
print(stu.get_score())#98

#特殊变量是__xx__，特殊变量可以直接访问，不是私有的，所以不能这样命名
#有的私有变量是_name，此时，我们应该按照规定，视为私有变量，不要使用
#__name私有变量实际上是，解释器把__name改成_Student_name，所以可以通过_Student_name来访问

#注意的地方：
stu.__name = 'New Name'
print(stu.__name)#New Name  此时是动态添加__name变量，而不是设置了__name变量
print(stu.get_name())#Baby   本身的私有变量还是没有被改变的


