#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:57
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_middle_school.py
# @Software: PyCharm


import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        # url = "https://vi.wikipedia.org/wiki/Danh_sách_trường_trung_học_phổ_thông_tại_Hà_Nội"
        url = "https://vi.wikipedia.org/wiki/Danh_sách_trường_trung_học_phổ_thông_tại_Thành_phố_Hồ_Chí_Minh"
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        response = etree.HTML(self.resp)
        # 河内
        # name = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr/td[1]//text()')
        # 胡志明
        name = response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr/td[2]//text()')
        name = [n.strip() for n in name if n != '\n']
        print(name)
        print(len(name))
        self.result = list(set(name))

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\middle_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
