#/usr/bin/env python3
#coding:utf-8


#XML两种解析方式：DOM和SAX，DOM把整个XML读入内存，占用内存大。SAX流模式，占用内存小
from xml.parsers.expat import ParserCreate
#使用SAX解析XML，通常关心的事件是start_element,end_element,char_data
'''
<a href='/'>python</a>
会产生3个事件：
1.start_element事件，读取<a href='/'>时
2.char_data事件，在读取python时
3.end_element事件，在读取</a>时
'''
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('star:%s attrs:%s' % (name, str(attrs)))
    def end_element(self, name):
        print('end:%s' % name)
    def char_data(self, text):
        print('char:%s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
print(parser.Parse(xml))
#读取一段字符串时，CharacterDataHandler可能被调用多次，需要先保存起来，在EndElementHandler里合并


#生成XML字符串
l = []
l.append(r'<?xml version="1.0"?>')
l.append(r'<root>')
l.append('some & data')
l.append(r'</root>')
print(''.join(l))#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
