#/usr/bin/env python3
#coding:utf-8


#itertools:用于操作迭代对象的函数
import itertools
# natuals = itertools.count(1)
# for n in natuals:
    # print(n)
#count()会创建一个无限的迭代器


# cs = itertools.cycle('ABC')
# for c in cs:
    # print(c)
#cycle()会把传入的一个序列无限重复下去


ns = itertools.repeat('A',3)
for n in ns:
    print(n)
#repeat()把一个元素无限重复下去，第二个参数可以指定重复次数，不指定就是无限重复


#takewhile()根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10, natuals)
print(list(ns))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#chain()把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'xyz'):
    print(c)


#groupby()把相邻的重复元素跳出来放到一起
for key,group in itertools.groupby('AaAcABBBCCCCCCAAA'):
    print(key, list(group))


#groupby增加函数规则
for key,group in itertools.groupby('AaAcABBBCCCCCCAAA', lambda c: c.upper()):
    print(key, list(group))


