#!/usr/bin/env python3
#coding:utf-8

#排序，sorted()函数
arr = sorted([1,44,3])
print(arr)#[1, 3, 44]

#自定义排序，按绝对值排序,key指定函数作用在每一个元素上，根据返回结果进行排序
arr = sorted([34,2,-45,-1],key=abs)
print(arr)#[-1, 2, 34, -45]

#对字符串进行排序，比较ascii大小
arr = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(arr)#['Credit', 'Zoo', 'about', 'bob']

#忽略大小写进行排序
arr = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(arr)#['about', 'bob', 'Credit', 'Zoo']

#进行反向排序
arr = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
print(arr)#['Zoo', 'Credit', 'bob', 'about']

#对一组元组进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L,key=by_name)
print(L2)#[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

#按成绩从高到低排序
def by_score(t):
    return t[1]
L2 = sorted(L,key=by_score,reverse=True)
print(L2)#[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]