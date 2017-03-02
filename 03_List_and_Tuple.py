#!/usr/bin/env python3
#coding:utf-8


#list：列表，一种有序的集合，可以随时添加和删除其中的元素。
students = ['a','b','c']
print(students)#['a', 'b', 'c']

#len()：获得list元素个数
print(len(students))#3

#可以用索引访问元素,超出范围会报错
print(students[0])#a

#获取最后一个元素，下方两种方法都可以
print(students[len(students)-1])#c
print(students[-1])#c

#倒数第2个，第3个
print(students[-2])#b
print(students[-3])#c

#append()：追加元素到末尾
students.append('dddd')
print(students)#['a', 'b', 'c', 'dddd']

#insert：插入元素到指定位置
students.insert(1,'aaaa')
print(students)#['a', 'aaaa', 'b', 'c', 'dddd']

#pop()：删除末尾元素
students.pop(1)
print(students)#['a', 'b', 'c', 'dddd']

#替换元素
students[1] = 'aaa'
print(students)#['a', 'aaa', 'c', 'dddd']

#list内元素数据类型可以不同
students.append(33)
print(students)#['a', 'aaa', 'c', 'dddd', 33]

#list内可以包含list
students.append(['cc',23])
print(students)#['a', 'aaa', 'c', 'dddd', 33, ['cc', 23]]

#list中没有元素，长度为0
students = []
print(len(students))#0


#tuple：元组，元组一旦初始化就不能修改,元组没有append()、insert()和赋值，其余方法和list一样
students = ('a','b','c')
print(students)#('a', 'b', 'c')

#元组定义时，元素就必须被确定下来

#空元祖
students = ()
print(students)#()

#只有一个元素的元组
students = (1,)
print(students)#(1,)

#元组中添加数组后，可以修改数组内容
students = ('a','b',['C','D'])
print(students)#('a', 'b', ['C', 'D'])
students[2][0] = 'c'
students[2][1] = 'd'
print(students)#('a', 'b', ['c', 'd'])
