#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 15:23
# @Author  : yangmingming
# @Site    : 
# @File    : weibo_spider.py
# @Software: PyCharm
import requests

session = requests.session()

url = "https://www.weibo.com/video/second?curr_tab=channel&type=icon&second_level_channel_id=4379553112491547&first_level_channel_id=4379553112491541&first_level_channel_name=时尚美妆&page_title=美妆教程"
header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "pragma": "no-cache",
    "sec-fetch-mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "sec-fetch-site": "none",
    "cookie": "SUB=_2AkMruX5Jf8NxqwJRmPoVxG7ka4l3yg7EieKd5Y-SJRMxHRl-yT9jqlwjtRB6ADlQpwU6MYjzKJ7Kqyb0LFLnkJNsBNgj; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWg20.RBHqipo9qTM2D_rC5; SINAGLOBAL=8696952143569.81.1558573436947; _ga=GA1.2.1066465571.1565058895; __gads=ID=3955d0108686b954:T=1565058897:S=ALNI_Mb4b0_xXuYr00umBBUIoICwP0wEpg; UOR=,,news.sweden.cn; ULV=1575947928312:20:1:1:7166641179238.531.1575947927694:1574996499470"

}

response = session.get(url=url, headers=header)
page_url = "https://www.weibo.com/video/aj/second?ajwvr=6&type=icon&second_level_channel_id=4379553112491547&editor_recommend_id=&since_id=4451165799120907&__rnd=1576742798962"
response = session.get(url=page_url, headers=header)
print(response.content.decode('gbk'))
