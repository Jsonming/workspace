#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 15:07
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_kompas_news.py
# @Software: PyCharm
import requests
url = 'https://money.kompas.com/home/more/5'
headers = {
    "referer": "https://money.kompas.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
resp = requests.post(url=url, headers=headers)
print(resp.text)

