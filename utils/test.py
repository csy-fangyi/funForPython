#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request

# 请求百度网页
resu = urllib.request.urlopen('http://www.baidu.com', data=None, timeout=10)
print(resu.read(300))

# 指定编码请求
f = urllib.request.urlopen('http://www.baidu.com')
print(f.read(100).decode('utf-8'))
