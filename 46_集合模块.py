#/usr/bin/env python3
#coding:utf-8


#collections:内建的集合模块，提供了许多有用的集合类

#namedtuple:创建自定义的tuple对象，并且规定了tuple元素的个数，可以用属性而不是索引来引用tuple的某个值
from collections import namedtuple
#name('name',[属性list])
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)#1 2
print(isinstance(p,Point))#True
print(isinstance(p,tuple))#True

#deque:deque除了实现list的append和pop外，还支持appendleft和popleft，这样尅搞笑的往头部添加或者删除元素
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
print(q)#deque(['a', 'b', 'c', 'x'])
q.appendleft('y')
print(q)#deque(['y', 'a', 'b', 'c', 'x'])

#defaultdict:如果key不存在，dict会抛出异常，如果希望返回一个默认值，就可以使用
from collections import defaultdict
d = defaultdict(lambda :'N/A')
print(d['kk'])#N/A
#默认值是调用函数返回，函数是在创建defaultdict对象时传入的

#orderedDict:如果需要dict保持key的顺序，可以使用ordereddict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)#{'b': 2, 'c': 3, 'a': 1}
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)#OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#按照key的插入顺序排序
#当容量超出时，会删除最早添加的key

#Counter:简单的计数器，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)#Counter({'r': 2, 'g': 2, 'm': 2, 'o': 1, 'n': 1, 'a': 1, 'i': 1, 'p': 1})
#counter实际上是dict的子类


