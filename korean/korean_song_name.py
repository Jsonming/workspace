#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 14:01
# @Author  : yangmingming
# @Site    : 
# @File    : korean_song_name.py
# @Software: PyCharm


import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://www.melon.com/chart/index.htm#params[idx]=51"
        url = "https://www.melon.com/chart/rise/index.htm#params[idx]=51"
        url = "https://www.melon.com/chart/day/index.htm#params[idx]=51"
        url = "https://www.melon.com/chart/week/index.htm#params[idx]=51&params[startDay]=20190429&params[endDay]=20190505&params[isFirstDate]=false&params[isLastDate]=true"
        url = "https://www.melon.com/chart/month/index.htm#params[idx]=51&params[rankMonth]=201904&params[isFirstDate]=false&params[isLastDate]=true"
        url = "https://www.melon.com/new/index.htm#params%5BareaFlg%5D=I&po=pageObj&startIndex={}".format(off_number)
        url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0100#params[gnrCode]=GN0100&params[dtlGnrCode]=&params[orderBy]=NEW&params[steadyYn]=N&po=pageObj&startIndex={}".format(off_number)
        url = "https://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=N".format(off_number)
        # url = "https://www.melon.com/genre/song_listPaging.htm?startIndex=6300&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=N"
        print(url)

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Cookie": "PCID=15572086739854917621858; PC_PCID=15572086739854917621858; POC=WP10"
        }
        response = requests.request("GET", url, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        html = etree.HTML(self.resp)
        # content = html.xpath('//*[@id="lst100"]/td[6]/div/div')
        # song_name = html.xpath('//*[@id="lst100"]/td[6]/div/div/div[1]/span/a/text()')
        # singer_name = html.xpath('//*[@id="lst100"]/td[6]/div/div/div[2]/a/text()')
        # content = html.xpath('//*[@id="frm"]/div/table/tbody/tr/td[5]/div/div')
        content = html.xpath('//*[@id="frm"]/div/table/tbody/tr/td[5]/div/div')

        for song_info in content:
            song_name = song_info.xpath('./div[1]/span/a/text()')[0]
            try:
                singer_name = song_info.xpath('./div[2]/a/text()')[0]
            except:
                singer_name = song_info.xpath('./div[2]/text()')[0]

            macth_one = re.findall('[a-zA-Z0-9]+', song_name)
            macth_two = re.findall('[a-zA-Z0-9]+', singer_name)

            if not macth_one and not macth_two:
                name = "{},{}".format(song_name, singer_name)
                print(name)
                self.result.append(name)

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\song_singer_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        for i in range(30000, 36000, 50):
            self.crawl(i)
            self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
