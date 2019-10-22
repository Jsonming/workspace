#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 18:20
# @Author  : yangmingming
# @Site    : 
# @File    : google_translate.py
# @Software: PyCharm


import requests
import re
import json
from spiderframe.script.google_translate_js import Py4Js


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        keyword = "you"
        pj = Py4Js()
        tk = pj.get_tk(keyword)
        url = "https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=0&tsel=0&kc=3&tk={tk}&q={keyword}".format(
            **locals())

        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        print(self.resp)
        dr = re.compile(r'<[^>]+>', re.S)
        response = json.loads(self.resp)[-1][0]
        for sentence in response:
            print(dr.sub('', sentence[0]))

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()

