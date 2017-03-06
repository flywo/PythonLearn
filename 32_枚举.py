#!/usr/bin/env python3
#coding:utf-8


#枚举
from enum import Enum
Month = Enum('Months', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#可以直接使用Month.jan来引用一个常亮或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)#依次打印
'''
Jan => Months.Jan , 1
Feb => Months.Feb , 2
Mar => Months.Mar , 3
Apr => Months.Apr , 4
May => Months.May , 5
Jun => Months.Jun , 6
Jul => Months.Jul , 7
Aug => Months.Aug , 8
Sep => Months.Sep , 9
Oct => Months.Oct , 10
Nov => Months.Nov , 11
Dec => Months.Dec , 12
'''
#value属性，是自动赋值给成员变量的int常量，默认从1开始
#如果需要更精确的控制枚举类型，可以从Enum派生出自定义类
from enum import unique
@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器帮助我们检查保证没有重复值
#访问枚举
print(Weekday.Sum)#Weekday.Sum
print(Weekday['Sum'])#Weekday.Sum
print(Weekday.Tue.value)#2
day = Weekday.Sum
print(day==Weekday.Sat)#False
print(Weekday(1))#Weekday.Mon
for name, member in Weekday.__members__.items():
    print(name, "=>", member)
'''
Sum => Weekday.Sum
Mon => Weekday.Mon
Tue => Weekday.Tue
Wed => Weekday.Wed
Thu => Weekday.Thu
Fri => Weekday.Fri
Sat => Weekday.Sat
'''
#成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
#Eunm可以把一组相关常量定义在一个class中，且class不可变，而且成员变量可以直接比较
