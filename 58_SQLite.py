#/usr/bin/env python3
#coding:utf-8


#要操作数据库，首先需要连接到数据库，一个数据库连接称为Connection，连接到后，需要打开游标，称之为Cursor
#通过Cursor执行SQL语句，然后获得执行结果
import sqlite3
#连接到数据库，如果不存在，自动创建
conn = sqlite3.connect('test.db')
#创建一个Cursor
cursor = conn.cursor()
#执行一条SQL语句，创建user表
cursor.execute('create table If Not Exists user (id varchar(20) primary key, name varchar(20))')
#插入一条记录
# cursor.execute('insert into user (id, name) values (\'3\', \'Michael\')')
#获得插入的行数
print(cursor.rowcount)
#关闭cursor
cursor.close()
#提交事务
conn.commit()
#管理connection
conn.close()

#查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#执行查询
cursor.execute('select * from user where id=?', '1')
print(cursor.fetchall())
cursor.close()
conn.close()

#cursor对象执行insert,update,delete语句时，执行结果由rowcount返回影响的行数，可以拿到执行结果
#执行select语句时，通过featchall()拿到结果，结果是一个list每个元素都是一个元组，对应一个记录
#如果sql语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个？占位符就必须对应几个参数
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))