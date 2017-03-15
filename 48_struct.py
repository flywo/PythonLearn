#/usr/bin/env python3
#coding:utf-8


#b'str'表示字节，所以字节数组=二进制str
#struct模块解决bytes和其它二进制数据类型的转换，pack函数把任意数据类型编程bytes
import struct
print(struct.pack('>I',1224009))
#b'\x00\x12\xadI'
#pack:第一个参数，处理指令
# '>I':>表示字节顺序是网络序，I表示4字节无符号整数，后面参数个数要和处理指令一致


#unpack把bytes变成相应的数据类型
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
#(4042322160, 32896)
#>IH:bytes一次变为I（4字节无符号整数）和H（2字节无符号整数）
#https://docs.python.org/3/library/struct.html#format-characters

