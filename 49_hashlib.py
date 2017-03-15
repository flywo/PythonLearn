#/usr/bin/env python3
#coding:utf-8


#hashlib提供了常见的摘要算法，比如MD5,SHA1等等
#摘要算法：又称哈希算法，散列算法，通过一个函数，把任意长度的数据转换为一个长度固定的数据串

#摘要算法，通过函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())#846014c3556d79e878be15fde5426e8a 32位16进制字符


#如果数据量大，可以分块多次调用update()，最后计算结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib'.encode('utf-8'))
print(md5.hexdigest())#846014c3556d79e878be15fde5426e8a


#另外一种摘要算法：SHA1
sha = hashlib.sha1()
sha.update('how to use sha1 '.encode('utf-8'))
sha.update('in python hashlib'.encode('utf-8'))
print(sha.hexdigest())#e9282e41aaf5ef53fd4ca3c191ed1e2546dbf3f2 40位16进制字符


#摘要算法应用：由于MD5码是一一对应的，所以保存重要数据时，就可以转换成MD5码后再保存到数据库
#防止MD5码被反推，可以给口令加盐
#明文+盐