#/usr/bin/env python3
#coding:utf-8


#把关系数据库的表结构映射到对象上,使用SQLAlchemy可以很方便实现
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#创建对象的基类
base = declarative_base()
#定义user对象
class User(base):
    #表名
    __tablename__ = 'user'
    #表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
#初始化数据库库连接
# Sqlite连接字符串中的/斜杠说明：三斜杠为相对路径，四斜杠为绝对路径。
engine = create_engine('sqlite:///test.db')


