#!/usr/bin/env python3
#coding:utf-8


#try
try:
    print('try...')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
'''
使用try来运行这段代码，如果出错，后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句，执行完毕except后，如果有finally语句，则执行
try...
except: division by zero
finally...
END
'''

#发生错误后，错误会有多个不同类型，应该由不同except语句处理
try:
    print('try...')
    r = 10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueErro:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:#如果没有错误，会执行else语句
    print('no error')
finally:
    print('finally...')
print('end')
'''
try...
ValueErro: invalid literal for int() with base 10: 'a'
finally...
end
'''

#所有错误都继承自BaseException，可以通过它捕获全部错误
try:
    foo()
except BaseException as e:
    print('发生了错误：',e)#发生了错误： name 'foo' is not defined

#常见错误类型：https://docs.python.org/3/library/exceptions.html#exception-hierarchy


#try...except可以跨越多层调用
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        print(bar('0'))
    except Exception as e:
        print('发生错误：',e)
    finally:
        print('finally...')
main()
'''
发生错误： division by zero
finally...
'''


#调用堆栈：如果错误没有被捕获，则会一直往上抛，最后被解释器捕获，打印一个错误，然后程序退出

#记录错误：如果不捕获错误，可以让解释器打印出错堆栈，但是程序也结束了。如果能捕获，就打印出来
#然后让程序继续执行，后面分析错误
#logging模块可以非常容易记录错误信息，可以通过logging把错误记录到文件里
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s)*2
def mian():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('End')


#抛出错误：因为错误是class，捕获异常实际上是捕获到该class的一个实例，错误也可以自定义
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        #执行后，这里会抛出错误
        raise FooError('invalid value: %s' % s)
    return 10 / n
# foo('0')


#如果处理不了错误，那么可以记录一下，把该错误继续往上抛出，让上层处理
#raise语句如果不带参数，就会把当前错误原样抛出，当然也可以通过raise语句
#抛出另外的一种错误
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10/n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise
# bar()
