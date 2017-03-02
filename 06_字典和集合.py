#!/usr/bin/env python3
#coding:utf-8


#Dict：也就是其它语言中的字典或者map。
names = ['Mi','Hi','You']
scores = [100,22,35]

#初始化字典
students = {'Mi':100,'Hi':22,'You':35}
print(students)#{'Mi': 100, 'You': 35, 'Hi': 22}

#添加元素
students['My'] = 56
print(students)#{'Hi': 22, 'Mi': 100, 'You': 35, 'My': 56}

#修改元素
students['My'] = 79
print(students)#{'You': 35, 'Mi': 100, 'Hi': 22, 'My': 79}

#取值时，如果key不存在会报错。避免该错误，方法一：
if 'My' in students:
    print(students['My'])#79
#方法二，通过dict提供的get方法，如果不存在，就返回None或者自己指定的值
print(students.get('MY'))#None
print(students.get('MY','没有key'))#没有key

#删除key
students.pop('My')
print(students)#{'Mi': 100, 'You': 35, 'Hi': 22}

#dict内部存放顺序和key放入顺序是没有关系的
#dict的key必须是不能改变的对象，比如字符串，整数等


#set：相当于字典key的集合，内部值不能重复，顺序也是无序的
students = set([1,2,3])
print(students)#{1, 2, 3}

#重复元素在set内会自动被过滤
students = set([1,1,2,3,4,5,5,5])
print(students)#{1, 2, 3, 4, 5}

#添加元素，可以重复添加，但不会有效果
students.add(7)
print(students)#{1, 2, 3, 4, 5, 7}

#删除元素
students.remove(1)
print(students)#{2, 3, 4, 5, 7}

#set实际上是数学意义上的无需和无重复元素的集合，所以set可以做交集，并集等操作
s1 = set([1,2,3])
s2 = set([3,4,5])
print(s1 & s2)#{3}
print(s1 | s2)#{1, 2, 3, 4, 5}

#set和字典一样，也不能放入可变元素
