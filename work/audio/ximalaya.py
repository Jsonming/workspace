#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 9:58
# @Author  : yangmingming
# @Site    :
# @File    : ximalaya.py
# @Software: PyCharm
import requests

headers = {
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'chrome-proxy': 'frfr',
    'Range': 'bytes=bytes=0-',
    'Referer': 'https://mobile.tingtingfm.com/v3/vod/2/VJLvsrKj0o',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

url = 'https://fdfs.xmcdn.com/group60/M08/5E/6C/wKgLb1y9kZ_jFQkAAEHSiD3AfCc181.m4a'

resp = requests.get(url, headers=headers)
with open('ting_ting_FM.mp3', 'ab')as f:
    f.write(resp.content)
print(resp)


