#!/usr/bin/env python3
#coding:utf-8


#调试：通过print()打印变量

#通过断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
#assert:表达式应该为true，表达式后面是错误描述，表达式如果不为true,assert就会抛出AssertionError
# main()

#启动解释器时，可以用-o参数来关闭assert，关闭后，所有的assert语句会被当成pass


#logging:把print替换为logging
import logging
logging.basicConfig(level=logging.INFO)
'''
logging可以指定记录信息的级别，有debug,info,warning,error等几个级别
当我们指定info时，logging.debug就不起作用了，同理指定warning后，debug
和info就不起作用了，这样，可以通过简单的配置，将一条语句同时输出到不同地方
'''
logging.info('info')


#pdb:启用python的调试器pdb，让程序单步的方式运行，可以随时查看运行状态
