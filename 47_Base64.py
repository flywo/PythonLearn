#/usr/bin/env python3
#coding:utf-8


#Base64是一种用64个字符来表示任意二进制数据的方法，Base64是一种场景的二进制编码方法
import base64
str = base64.b64encode(b'binary\x00string')
print(str)#b'YmluYXJ5AHN0cmluZw=='
str = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(str)#b'binary\x00string'

#url中的base64编码，把+/转换成-_
str = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(str)#b'abcd++//'
str = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(str)#b'abcd--__'


#还可以自定义64个字符的排列顺序，就可以自定义base64编码
#=编码后会被去掉
# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'

#base64是一种任意二进制到文本字符串的编码方法，常用语url,cookie,网页中传输少量的二进制数据
