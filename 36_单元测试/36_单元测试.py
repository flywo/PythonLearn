#!/usr/bin/env python3
#coding:utf-8


#单元测试：测试一个模块一个函数或者一个类来进行正确性的检验工作
#编写测试Dict模块的测试代码
'''
测试类，需要继承自unittest.TestCase
以test开头的方法就是测试方法，不以test开头，不会被执行
assertEqual(abs(-1),1):断言函数返回的结果与1相等
assertRaises:断言抛出异常
'''
import unittest
from Dict import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

