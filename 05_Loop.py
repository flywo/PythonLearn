#!/usr/bin/env python3
#coding:utf-8


#循环语句
#for...in：一次迭代数组和元组中元素
students = ['a','b','c']
for name in students:
    print(name)#a b c

#range()：生成一个整数序列，再通过list()函数转换成list，比如range(2)表示从0到2的序列
students = list(range(11))
print(students)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for x in range(11):
    sum = sum + x
print(sum)#55


#while循环：条件不满足时推出循环
sum = 0
n = 10
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)#30


#break：跳出当前循环
while n <= 15:
    if n == 10:
        break
    print(n)#打印到9就没有了
    n+=1


#continue：跳过当前循环，进行下一个循环
while n <= 25:
    n += 1
    if n == 20:
        continue
    print(n)#跳过了20


