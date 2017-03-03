#!/usr/bin/env python3
#coding:utf-8


#匿名函数：传入函数时，有时候，不需要显示的定义函数，传入匿名函数更方便,lambda表示匿名函数
arr = list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
print(arr)#[1, 4, 9, 16, 25, 36, 49, 64, 81]

#lambda x: x*x实际上就是：def f(x): return x*x
#lambda:表示匿名函数   x：表示匿名参数
#匿名函数只能有一个表达式，用些return，返回值就是表达式结果
#匿名函数没有名字，不用担心函数名冲突，匿名函数也是一个函数对象，也可以赋值，在利用变量来调用该函数
f = lambda s:s*s
print(f(10))#100

#匿名函数也可以做为返回值
def build(x,y):
    return lambda: x*x+y*y
f = build(4,5)
print(f())#41

