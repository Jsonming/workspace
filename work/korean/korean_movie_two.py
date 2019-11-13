#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 10:40
# @Author  : yangmingming
# @Site    : 
# @File    : korean_movie_two.py
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
        url = "https://movie.naver.com/movie/running/current.nhn"
        url = "https://movie.naver.com/movie/running/premovie.nhn"
        url = "https://movie.naver.com/movie/running/movieclip.nhn"
        url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20190506"
        url = "https://movie.naver.com/movie/sdb/browsing/bmovie_nation.nhn"
        url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}".format(off_number)
        print(url)
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
        html = etree.HTML(self.resp)
        names = []
        # names_content_list = html.xpath('//*[@id="content"]/div[1]/div[1]/div/ul/li/dl/dt/a/text()')
        # names_content_table = html.xpath('//*[@id="content"]/div[1]/div[2]/div/div/ol/li/a/p/text()')

        # names_content_list = html.xpath('//*[@id="old_content"]/table/tbody/tr/td/div/a/text()')
        # names_content_table = html.xpath('//*[@id="assistant"]/div/ul/li/a/text()')

        # names_content_table = html.xpath('//*[@id="old_content"]/dl/dd/ul/li/a/text()')
        names_content_table = html.xpath('//*[@id="old_content"]/table/tbody/tr/td[4]/a[1]/text()')

        # names.extend(names_content_list)
        names.extend(names_content_table)
        for name in names:
            name = pattern.sub('', name)
            macth = re.findall('[a-zA-Z0-9]+', name)
            if not macth:
                name = name.strip()
                print(name)
                self.result.append(name)

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\movie_name_two.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        for i in range(1000, 3000):
            self.crawl(i)
            self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
