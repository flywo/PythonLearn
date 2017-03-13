#/usr/bin/env python3
#coding:utf-8


#datetime是处理日期和时间的标准库
#获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now)#2017-03-13 16:43:46.499538
print(type(now))#<class 'datetime.datetime'>  datetime模块，datetime类

#获得指定某个日期和时间
dt = datetime(2017, 3, 12, 12, 20)
print(dt)#2017-03-12 12:20:00

#datetime转换为timestamp:timestamp是固定的，可以转换时区
dt = datetime(2018, 1, 1, 12, 12)
print(dt.timestamp())#1514779920.0  小数位表示毫秒

#timestamp转换datetime
t = 1514779920.0
print(datetime.fromtimestamp(t))#2018-01-01 12:12:00

#datetime是有时区的，默认是本地时区
#转换成utc时间
print(datetime.utcfromtimestamp(t))#2018-01-01 04:12:00

#str转换成datetime
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
cday = datetime.strptime('2018-01-01 04:12:00', '%Y-%m-%d %H:%M:%S')
print(cday)#2018-01-01 04:12:00
#转换后的datetime是没有时区信息的

#datetime转换成str
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))#Mon,Mar 13 17:07

#datetime加减，需要导入timedelta
from datetime import timedelta
now = datetime.now()
print(now)#2017-03-13 17:09:13.287169
now += timedelta(hours=10)
print(now)#2017-03-14 03:10:19.592955
now -= timedelta(hours=10)
print(now)#2017-03-13 17:10:52.576688
now -= timedelta(days=1)
print(now)#2017-03-12 17:11:44.898058

#本地时间转换成UTC时间
#datetime类型有一个时区属性tzinfo，默认为none
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))#创建时区UTC+8:00
now = datetime.now()
print(now)#2017-03-13 17:13:47.730967
dt = now.replace(tzinfo=tz_utc_8)
print(dt)#2017-03-13 17:15:36.031776+06:00

#时区转换
#强制设置成utc+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone()转换成北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)#2017-03-13 17:19:02.941718+08:00
#转成东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)#2017-03-13 18:20:39.584141+09:00
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
#拿到一个datetime，获知正确时区，然后强制设置时区，作为基准时间，利用带时区的datetime
#通过astimezone方法转换到任意时区