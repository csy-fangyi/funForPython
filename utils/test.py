#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib import request

# 请求百度网页
resu = request.urlopen('http://www.baidu.com', data=None, timeout=10)
print(resu.read())

# 指定编码请求
f = request.urlopen('https://www.chuangcache.com')
print(f.read().decode('utf-8'))
