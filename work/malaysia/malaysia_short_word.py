#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 18:01
# @Author  : yangmingming
# @Site    : 
# @File    : malaysia_short_word.py
# @Software: PyCharm


import requests
import re
import json
import os
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "http://id.nemoapps.com/phrasebooks/malay"
        url = "http://www.ekamus.info/"
        url = "https://uccae5e2742a82972a6e3c77c8be.previews.dropboxusercontent.com/p/pdf_img/AAbipkWs_Ccka-zCjDNry5ZqN0QAcArNj6YftzJlYMUQhFXqL3oxhJPeBW5bmNDLakKNU2pyiX8L5h4EKbSmoug_pWPOvBAGgKDcwd3vE3oJxbzFGR5-LC2ZlbQ_zuLLhECtHQN8lTgW59iM2iYsoE3PwgE4mdB52DKLUmD6vbw1HZT1odhXan25VKMIgAY5if7_R0eCsNjdiizwX4D16vCQKYtLkTsV0VXrWOyntrycqQPlwEYpm966KBydkyQE8gXvnqPfvfx-upxLS0Y6sfWHNOiSQaQmYhi6TFxUnDfxcKKobCQX3N-tqpMu0sUeyec82yOE7JQ8WkW8GQKayIAAU5EGw_GZhk3muSyTdpAmnA/p.png?page=0&scale_percent=0"
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        print(self.resp)

        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)
        # names = []

        # html = etree.HTML(self.resp)
        # name_one = html.xpath('//td[@class="scripts-column"]/div[1]/strong/text()')
        # name_two = html.xpath('//td[@class="scripts-column"]/div[2]/strong/text()')
        # names.extend(name_one)
        # names.extend(name_two)
        # print(names)
        # self.save(names)

        # html = etree.HTML(self.resp.replace('<?xml version="1.0" encoding="UTF-8"?> ', ''))
        # names = html.xpath('/html/body/div[2]/table[1]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[2]/a/text()')
        # self.save(names)

        html = etree.HTML(self.resp.replace('<?xml version="1.0" encoding="UTF-8"?> ', ''))
        names = html.xpath('//*[@id="_CJraXPGSEpXu8wW0jLioCQ25"]/div/div/div[38]/a/div/div[3]/div')
        # self.save(names)
        print(names)

    def save(self, result):
        folder = r"C:\Users\Administrator\Desktop\malaya_temp"
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(r'{}\short_word.txt'.format(folder), 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
