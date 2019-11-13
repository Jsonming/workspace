#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 16:17
# @Author  : yangmingming
# @Site    : 
# @File    : vietanm_short_word.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "http://tratu.coviet.vn/hoc-tieng-trung/tu-dien/lac-viet/T-V/{}.html".format(off_number)
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)

        html = etree.HTML(self.resp)
        names = html.xpath('//*[@id="partofspeech_0"]/div/span/text()')
        print(names)
        pattern_eight = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
        pattern_four = re.compile("[\u4e00-\u9fa5]+", re.S)  # 中文
        pattern_three = re.compile("[0-9]+|\.", re.S)
        pattern_seven = re.compile(u"[\u3000-\u303f\ufb00-\ufffd]+")  # 标点符号
        pattern_nine = re.compile("[\.\!\/_,,$%^*(+\"\'——！，。？、~@#￥%……&*（）]+")  # 标点符号
        name_data = []
        for name in names:
            name = re.sub(pattern_eight, '', name)
            name = re.sub(pattern_four, '', name)
            name = re.sub(pattern_three, '', name)
            name = re.sub(pattern_seven, '', name)
            name = re.sub(pattern_nine, '', name)
            name = name.strip()
            print(name)
            self.save(name)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\vietnam\short_word.txt', 'a', encoding='utf-8')as f:
            f.write(result + "\n")

    def run(self):
        file = r"C:\Users\Administrator\Desktop\vietnam\chinese_word.txt"
        with open(file, 'r', encoding='utf8')as f:
            for word in f:
                self.crawl(word.strip())
                self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
