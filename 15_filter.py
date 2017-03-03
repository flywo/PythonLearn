#!/usr/bin/env python3
#coding:utf-8


#filter：过滤序列，接收一个函数和一个序列，filter把传入的函数依次作用于每个元素，根据返回True还是False决定保留还是丢弃
#删除掉偶数
def is_odd(n):
    return n%2==1
arr = list(filter(is_odd,[1,2,3,4,5,6]))
print(arr)#[1, 3, 5]

#删除掉空字符
def not_empty(s):
    return s and s.strip()
arr = list(filter(not_empty,['a','','c',None,' ']))
print(arr)#['a', 'c']


