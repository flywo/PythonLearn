#!/usr/bin/env python3
#coding:utf-8

#继承
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
cat = Cat()
dog.run()#Animal is running...
cat.run()#Animal is running...

#可以给子类增加方法
class Dog(Animal):
    def run(self):
        print('Dog running...')
dog = Dog()
dog.run()#Dog running...

#多态
animal = Animal()
dog = Dog()
animal.run()#Animal is running...
dog.run()#Dog running...

#函数接收对象
def run_once(animal):
    animal.run()
run_once(animal)#Animal is running...
run_once(dog)#Dog running...


