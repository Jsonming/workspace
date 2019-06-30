#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 17:06
# @Author  : yangmingming
# @Site    : 
# @File    : youtu_song_name.py
# @Software: PyCharm

import requests
import json
import re
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://www.youtube.com/playlist"
        querystring = {"list": "PLgNjz5kKawRiPXT7l3XT60v3iWogBvGP0"}
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        self.resp = response.text

    def parser(self):
        response = re.findall(r'window\["ytInitialData"] = (.*?);', self.resp)[0]
        response = json.loads(response)
        video_list = response["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"][
            "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["playlistVideoListRenderer"][
            "contents"]

        for video in video_list:
            name_lable = video["playlistVideoRenderer"]["title"]["simpleText"]
            name_lable = name_lable.split('-')
            name_lable = name_lable[1] if len(name_lable) > 1 else name_lable[0]
            if '(' in name_lable:
                name = name_lable.split('(')[0]
            else:
                name = name_lable
            name = name.strip()
            self.result.append(name)

    def save(self):
        with open('C:\\Users\\Administrator\\Desktop\\song.txt', 'a', encoding='utf-8')as f:
            f.write(','.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
