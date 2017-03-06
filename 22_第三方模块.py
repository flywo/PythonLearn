#!/usr/bin/env python3
#coding:utf-8


#python中，第三方模块是通过pip管理的

#模块路径：当我们试图加载一个模块时，python会在指定的路径下搜索对应的.py文件，如果找不到会报错

#python默认会搜索当前目录、所有已安装的内置模块和第三方模块。搜索路劲存放在sys模块的path变量中
import sys
print(sys.path)#['/Users/baiwei/Desktop/baiwei/python/PythonLearn',
# '/Users/baiwei/Desktop/baiwei/python/PythonLearn',
# '/Library/Frameworks/Python.framework/Versions/3.5/lib/python35.zip',
#  '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5',
# '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin',
#  '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload',
# '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages']

#如果我们需要自己添加搜索目录需要修改sys.path，添加搜索的目录
#方法一：sys.path.append('/Users/michael/my_py_scripts')，该方法运行时修改，运行结束失败
#方法二：设置环境变量PYTHONPATH,该变量的内容会被自动添加到模块搜索路径中，设置方法与设置path环境变量类似
#       注意只需要添加自己的搜索路径，本身路径不受影响



