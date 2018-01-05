#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import re
import sys
from urllib import request


class Beian(object):
    gongan_api = 'http://www.sojson.com/api/gongan/'
    icp_api = 'http://www.sojson.com/api/beian/'
    check = '(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$'

    def __init__(self, domain, type):
        self.domain = domain
        self.type = type

    def output(self):
        if re.match('(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$', self.domain) == None:
            print('--error domain--')
        else:
            if self.type == 'icp':
                icp_beian(self)
            else:
                gongan_beian(self)


def icp_beian(self):
    rep = request.urlopen(self.icp_api + self.domain)
    # rep = requset.urlopen(api+domain) #python3
    page = rep.read()
    page = page.decode('utf-8')
    # page_dict = eval(page) #使用eval字符串转换字典，需指定null为空
    page_dict = json.loads(page)
    if 'status' in page_dict == True and page_dict['status'] == 304:  # python2 此处用has_key
        print("\033[1;31;40m [请求太频繁。] \033[0m")
    elif page_dict["type"] == 300:
        print("\033[1;31;40m [没有查询到备案信息，或者是新备案的域名。] \033[0m")
    else:
        page_info = (
            "备案性质：{nature},"
            "主备案号：{icp},"
            "首页：{indexUrl},"
            "备案的名称：{sitename},"
            "备案的一级域名：{domain},"
            "当前域名备案号：{nowIcp},"
            "备案状态：{type1},"
            "查询的信息：{search},"
            "备案检查时间：{checkDate},"
            "备案主体：{name}"
                .format(
                nature=page_dict['nature'],
                icp=page_dict['icp'],
                indexUrl=page_dict['indexUrl'],
                sitename=page_dict['sitename'],
                domain=page_dict['domain'],
                nowIcp=page_dict['nowIcp'],
                type1=page_dict['type'],
                search=page_dict['search'],
                checkDate=page_dict['checkDate'],
                name=page_dict['name'],
            )
        )
        page_list = page_info.split(',')
        print(('=' * 5) + "ICP备案信息" + ('=' * 5))
        for i in page_list:
            print(i)
        print('=' * 20)


def gongan_beian(self):
    rep = request.urlopen(self.gongan_api + self.domain)
    # rep = requset.urlopen(api+domain) #python3
    page = rep.read()
    page = page.decode('utf-8')
    # page_dict = eval(page) #使用eval字符串转换字典，需指定null为空
    page_dict = json.loads(page)

    if page_dict["status"] == 404:
        print("\033[1;31;40m [没有查询到备案信息，或者是新备案的域名。] \033[0m")
    else:
        data = page_dict['data']
        data_info = (
            "备案号：{id},"
            "网站名：{sitename},"
            "网站域名：{sitedomain},"
            "网站类型：{sitetype},"
            "备案时间：{cdate},"
            "开办主体：{comtype},"
            "开办者名称：{comname},"
            "备案机关：{comaddress},"
            "更新时间：{updateTime}"
                .format(
                id=data['id'],
                sitename=data['sitename'],
                sitedomain=data['sitedomain'],
                sitetype=data['sitetype'],
                cdate=data['cdate'],
                comtype=data['comtype'],
                comname=data['comname'],
                comaddress=data['comaddress'],
                updateTime=data['updateTime'],
            )
        )
        date_list = data_info.split(',')
        print(('=' * 5) + "公安备案信息" + ('=' * 5))
        for i in date_list:
            print(i)
        print('=' * 20)


if __name__ == '__main__':
    beian = Beian(sys.argv[1], sys.argv[2])
    beian.output()
