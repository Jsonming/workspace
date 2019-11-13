#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 16:39
# @Author  : yangmingming
# @Site    : 
# @File    : korean_sights.py
# @Software: PyCharm


import requests
import re
import json
from lxml import etree

pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://blog.naver.com/PostView.nhn?blogId=inzzang9807&logNo=221437865470&redirect=Dlog&widgetTypeCall=true&directAccess=false"
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            # "Cookie": "NNB=ENAXSR4X7DHVY; page_uid=ULZ8nspVuE0sstByT/Vssssstyl-325780; nx_ssl=2; JSESSIONID=9EF2927E83C53B902F0166C9A7E0CB5F.jvm1",
            # "Referer": "https://blog.naver.com/PostView.nhn?blogId=inzzang9807&logNo=221437865470&redirect=Dlog&widgetTypeCall=true&directAccess=false",
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        html = etree.HTML(self.resp)
        sights = html.xpath('//*[@id="post-view221437865470"]/table/tbody/tr/td[2]//span/text()')
        for sight in sights:
            sight = sight.strip()
            sight = pattern.sub('', sight)
            sight = sight.strip()
            if sight:
                macth = re.findall('[a-zA-Z0-9]+', sight)
                if not macth:
                    sight = sight.split(',')[-1]
                    sight = sight.strip()
                    self.result.append(sight)

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\sights_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
