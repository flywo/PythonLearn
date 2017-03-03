#!/usr/bin/env python3
#coding:utf-8

#函数可作为返回值
#普通可变参数求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

#返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
result = lazy_sum(1,2,3,4,5)
print(result)#<function lazy_sum.<locals>.sum at 0x10137d730>
print(result())#15

#每次调用lazy_sum时，都会返回一个新的函数，即使传入相同的参数
result1 = lazy_sum(1,2,3,4,5)
print(result1==result)#False


#闭包：返回函数在内部引用了局部变量，当一个函数返回了一个函数后，其内部的局部变量还是被新函数引用
#返回函数没有立即执行，只有调用了f()才执行
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
#最终f1(),f2(),f3()结果都是9，因为函数没有立即执行，3个函数都返回时，
#引用的i已经变成3了。所以：返回函数不要引用任何循环变量，或者后续会发生变化的变量