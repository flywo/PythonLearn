#!/usr/bin/env python3
#coding:utf-8


#操作文件和目录，可以在命令行输入dir，cp等，在ptyhon中，内置的os模块可以
#直接调用操作系统提供的接口函数
import os
print(os.name)#posix:说明系统是linux、unix、mac os x，如果是nt就是windows


#uname()函数：获取详细的系统信息，该函数在windows上不提供
print(os.uname())#posix.uname_result(sysname='Darwin',
# nodename='baiweideMacBook-Pro.local',
# release='15.6.0',
# version='Darwin Kernel Version 15.6.0: Thu Jun 23 18:25:34 PDT 2016;
# root:xnu-3248.60.10~1/RELEASE_X86_64', machine='x86_64')


#环境变量：操作系统的环境变量，全部保存在os.environ这个变量中
print(os.environ)#environ({'rvm_prefix': '/Users/baiwei',
# 'rvm_bin_path': '/Users/baiwei/.rvm/bin',
# 'XPC_FLAGS': '0x0',
# '_system_version': '10.11',
# '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34',
#  'SHELL': '/bin/bash',
# 'rvm_path': '/Users/baiwei/.rvm',
# 'GEM_HOME': '/Users/baiwei/.rvm/gems/ruby-2.2.2',
# 'PYCHARM_HOSTED': '1',
# 'LC_CTYPE': 'zh_CN.UTF-8',
# 'VERSIONER_PYTHON_VERSION': '2.7',
#  'PYTHONIOENCODING': 'UTF-8', 'GEM_PATH': '/Users/baiwei/.rvm/gems/ruby-2.2.2:/Users/baiwei/.rvm/gems/ruby-2.2.2@global', 'rvm_loaded_flag': '1', 'LOGNAME': 'baiwei', 'PATH': '/Library/Frameworks/Python.framework/Versions/3.5/bin:/Users/baiwei/.rvm/gems/ruby-2.2.2/bin:/Users/baiwei/.rvm/gems/ruby-2.2.2@global/bin:/Users/baiwei/.rvm/rubies/ruby-2.2.2/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/Users/baiwei/.rvm/bin', 'IRBRC': '/Users/baiwei/.rvm/rubies/ruby-2.2.2/.irbrc', '_system_name': 'OSX', 'RUBY_VERSION': 'ruby-2.2.2', 'TMPDIR': '/var/folders/00/9krg2ct91tvg6kd_t543z4qw0000gn/T/', 'PYTHONPATH': '/Users/baiwei/Desktop/baiwei/python/PythonLearn', 'rvm_user_install_flag': '1', 'DISPLAY': '/private/tmp/com.apple.launchd.xKOJKSBlM6/org.macosforge.xquartz:0', 'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'USER': 'baiwei', 'HOME': '/Users/baiwei', '_system_arch': 'x86_64', '_system_type': 'Darwin', 'PYTHONUNBUFFERED': '1', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.z2XqEXrMW7/Listeners', 'rvm_stored_umask': '0022', 'rvm_version': '1.27.0 (latest)', 'MY_RUBY_HOME': '/Users/baiwei/.rvm/rubies/ruby-2.2.2', '__PYVENV_LAUNCHER__': '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5', 'XPC_SERVICE_NAME': '0', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.dXQiW3Iw4H/Render'})


#os.environ.get('key')：获得某个环境变量的值
print(os.environ.get('PATH'))#/Library/Frameworks/Python.framework/Versions/3.5/bin:/Users/baiwei/.rvm/gems/ruby-2.2.2/bin:/Users/baiwei/.rvm/gems/ruby-2.2.2@global/bin:/Users/baiwei/.rvm/rubies/ruby-2.2.2/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/Users/baiwei/.rvm/bin
print(os.environ.get('x','default'))#default：如果没有取到显示默认


#操作文件和目录
#一部分在os模块中，一部分在os.path模块中
#查看、创建和删除目录

#查看当前目录的绝对路径
print(os.path.abspath('.'))#/Users/baiwei/Desktop/baiwei/python/PythonLearn

#在某个目录下创建一个新的目录，首先把新的目录的完整路径给标示出来：
print(os.path.join('/Users/baiwei/Desktop/','Test'))#/Users/baiwei/Desktop/Test

#创建一个目录
os.mkdir('/Users/baiwei/Desktop/Test')

#删除掉一个目录
os.rmdir('/Users/baiwei/Desktop/Test')

#合成路径时，不要直接拼接字符串，而是通过os.path.join()函数，这样可以正确处理不同
#操作系统的路径分割

#拆分路径时也是不要直接去拆，通过os.path.split()函数，把路径拆分
#为两部分，后一部分是最后级别的目录或文件名
print(os.path.split('/Users/baiwei/Desktop/Test'))
#('/Users/baiwei/Desktop', 'Test')

#os.path.splitext()可以直接得到文件扩展名
print(os.path.splitext('/Users/baiwei/Desktop/Test.text'))
#('/Users/baiwei/Desktop/Test', '.text')


#文件操作，假定目录下右一个test.txt文件
#重命名
# os.rename('test.txt','test.py')

#删除文件
# os.remove('test.py')


#shutil模块提供copyfile()函数，可以复制

#过滤文件
#列出当前目录下所有的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#['.git', '.idea', '33_元类', '36_单元测试', '37_文件读写']


#列出所有py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
