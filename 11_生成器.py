#!/usr/bin/env python3
#coding:utf-8

#列表生成式：列表元素按照某种算法推算出来
#通过列表生成式的[]改成()创建generator
arr = [x*x for x in range(10)]
print(arr)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
generator = (x*x for x in range(10))
print(generator)#<generator object <genexpr> at 0x1013827d8>

#打印generator的元素
print(next(generator))#0
print(next(generator))#1
print(next(generator))#4
print(next(generator))#9  没有更多元素会抛出异常

#通过for循环迭代generator
for n in generator:
    print(n)#0, 1, 4, 9, 16, 25, 36, 49, 64, 81

#将函数编程生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return "done"
#如果一个函数定义中包含yield关键字，那么该函数就是一个generator，不再是普通的函数
print(fib(6))#<generator object fib at 0x101382830>

#每次generator遇到yield语句时，会返回，再次执行时从返回处继续执行
def add():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)
    yield 3
arr = add()
next(arr)#1
next(arr)#2
next(arr)#3
#用for循环遍历
for n in fib(6):
    print(n)

#杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]
n = 0
for t in triangles():
    print(t)
    n = n+1
    if n == 10:
        break
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''
