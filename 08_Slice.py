#!/usr/bin/env python3
#coding:utf-8


#切片
student = ['a','b','c','d']
print(student[0:2])#['a', 'b']

#如果是第0个索引，还可以省略
print(student[:2])#['a', 'b']

#倒数切片,倒数第一个元素是-1
print(student[-2:])#['c', 'd']

#切片示例：
#获取前10个元素
student = list(range(100))
print(student[:10])#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#前11-20个元素
print(student[10:20])#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#前10个数，每两个取一个
print(student[:10:2])#[0, 2, 4, 6, 8]
#所有数，每10个取一个
print(student[::10])#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
#什么都不写，就是复制
print(student[:])#[0...100]

#元组也可以进行切片，结果仍然是元组
student = (1,2,3,4,5)[:3]
print(student)#(1, 2, 3)

#字符串也是一种list，也可以进行切片
student = 'abcdefg'[:4]
print(student)#abcd

