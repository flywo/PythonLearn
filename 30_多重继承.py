#!/usr/bin/env python3
#coding:utf-8


#多重继承
class Animal(object):
    pass
#大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#我们要给动物加上Runnable和Flyable功能
class Runable(object):
    def run(self):
        print('Running...')
class FlyAble(object):
    def fly(self):
        print('Flying...')
#如果需要一个runable的动物，就多继承一个
class Dog(Mammal, Runable):
    pass
#这样，Dog就同时继承了Mammal和Runable的所有功能
dog = Dog()
dog.run()#Running...

#我们可以把Runable改成runableMixIn，表示是混合，父类是Mammal