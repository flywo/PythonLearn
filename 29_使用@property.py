#!/usr/bin/env python3
#coding:utf-8


#可以使用set_score()和get_score()方法来检查参数
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('不是整数！')
        if value < 0 or value > 100:
            raise ValueError('必须是0--100')
        self._score = value
s = Student()
s.set_score(60)
print(s.get_score())#60
#s.set_score(999)#报错
#s.set_score('2')#报错

#@property装饰器负责把一个方法变成属性调用
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('不是整数！')
        if value < 0 or value > 100:
            raise ValueError('必须是0--100')
        self._score = value
#@property把一个getter方法变成属性，@score.setter把一个setter变成属性赋值
s = Student()
s.score = 89#实际上是s.set_score(60)
print(s.score)#89  实际上是s.get_score(60)

#还可以只定义getter方法，setter方法等
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2017-self._birth
#age就是只读，根据birth计算出来
s = Student()
s.birth = 1989
print(s.birth)#1989
print(s.age)#28
