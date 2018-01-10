#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import re
import sys
from urllib import request


class Beian(object):
    gongan_api = "http://www.sojson.com/api/gongan/"
    icp_api = "http://www.sojson.com/api/beian/"
    check = "(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$"

    def __init__(self, domain, type):
        self.domain = domain
        self.type = type

    def doGet(self, url):
        rep = request.urlopen(url)
        page = rep.read().decode("utf-8")
        return json.loads(page)

    def icp_beian(self):
        page_dict = self.doGet(self.icp_api + self.domain)
        if page_dict.get('status', '') == 304:
            return {"msg": "请求太频繁。"}
        elif page_dict.get('type', '') == 300:
            return {"msg": "没有查询到备案信息，或者是新备案的域名。"}
        else:
            data = {}
            data["备案性质"] = page_dict["nature"]
            data["主备案号"] = page_dict["icp"]
            data["首页"] = page_dict["indexUrl"]
            data["备案的名称"] = page_dict["sitename"]
            data["备案的一级域名"] = page_dict["domain"]
            data["当前域名备案号"] = page_dict["nowIcp"]
            data["查询的信息"] = page_dict["search"]
            data["备案检查时间"] = page_dict["checkDate"]
            data["备案主体"] = page_dict["name"]
            return data

    def gongan_beian(self):
        page_dict = self.doGet(self.gongan_api + self.domain)

        if page_dict.get('status', '') == 200:
            data = {}
            data["备案号"] = page_dict["data"]["id"]
            data["网站名"] = page_dict["data"]["sitename"]
            data["网站域名"] = page_dict["data"]["sitedomain"]
            data["网站类型"] = page_dict["data"]["sitetype"]
            data["备案时间"] = page_dict["data"]["cdate"]
            data["开办主体"] = page_dict["data"]["comtype"]
            data["开办者名称"] = page_dict["data"]["comname"]
            data["备案机关"] = page_dict["data"]["comaddress"]
            data["更新时间"] = page_dict["data"]["updateTime"]
            return data
        else:
            return {"msg": str(page_dict["status"])}

    def output(self):
        if re.match("(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$", self.domain) == None:
            print("--error domain--")
        else:
            if self.type == "icp":
                data = self.icp_beian()
            else:
                data = self.gongan_beian()
            if data == "" or data == None:
                print("--error info--")
            else:
                print(("=" * 5) + "备案信息" + ("=" * 5))
                for i in data:
                    print(i + " : " + data[i])
                print("=" * 20)


if __name__ == "__main__":
    beian = Beian(sys.argv[1], sys.argv[2])
    beian.output()
