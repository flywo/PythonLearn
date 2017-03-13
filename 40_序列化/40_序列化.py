#!/usr/bin/env python3
#coding:utf-8


#序列化：把变量从内存变成可存储或传输的过程称之为序列化
#序列化之后就可以写入磁盘，或者传输到别的机器上

#反序列化：把对象重新读到内存中称为反序列化

#pickle模块实现序列化
import pickle
d = dict(name='Bob', age=20, score= 99)
print(pickle.dumps(d))
#b'\x80\x03}q\x00(X\x05\x00\x00\x00scoreq\x01KcX\x03\x00\x00\x00ageq\x02K\x14X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
#pickle.dumps方法把对象序列化成一个bytes，然后就可以写入文件或者使用
#pickle.dump()直接把对象序列化后写入一个file-like object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
#写入了dump.txt文件


#从dump.txt文件中读取对象：先把内容读到一个bytes中，然后用pickle.loads()方法
#反序列化出对象，或者直接使用pickle.load()从file-like object中反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)#{'name': 'Bob', 'score': 99, 'age': 20}


#JSON:把对象序列化为json
'''
JSON类型               Python类型
{}                     dict
[]                     list
"string"               str
123.3                  int或float
true/false             True/False
null                   None
'''

#json模块提供非常完善的对象到json格式的转换
import json
d = dict(name='B',age=90,score=0)
print(json.dumps(d))#{"name": "B", "age": 90, "score": 0}

#dump()方法可以把JSON对象写入file-like object
f = open('json.txt', 'w')
json.dump(d, f)
f.close()

#把json反序列化成python对象用loads()或load()，前者反序列化字符串，后者从file-like object中读取字符串并反序列化
str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(str))#{'name': 'Bob', 'age': 20, 'score': 88}

#load()
f = open('json.txt', 'r')
print(json.load(f))#{'name': 'B', 'score': 0, 'age': 90}
f.close()


#JSON进阶
#https://docs.python.org/3/library/json.html#json.dumps
#序列化一个自定义对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):#该函数将对象转换成dict
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
#对象转json
s = Student('angle',33,45)
print(json.dumps(s,default=student2dict))#{"score": 45, "age": 33, "name": "angle"}


#将任意class的实例变为dict,每个class都有一个__dict__属性，是一个dict，存储实例变量
print(json.dumps(s,default=lambda obj:obj.__dict__))
#{"age": 33, "score": 45, "name": "angle"}


#将json反序列化为一个对象，用loacs()方法转换出dict对象，然后传入
#object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
#<__main__.Student object at 0x10141fcc0>反序列化出对象

