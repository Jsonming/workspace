#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 9:20
# @Author  : yangmingming
# @Site    : 
# @File    : ting_ting_FM.py
# @Software: PyCharm
import requests

headers = {
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Range': 'bytes=32768-',
    'Referer': 'https://mobile.tingtingfm.com/v3/vod/2/VJLvsrKj0o',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

url = 'https://ttfm2018-oss-cdn.tingtingfm.com/audio/radio/2019/0525/a1/2e/a12e854fe064a638eb59e938f3a6d0cf.m4a?auth_key=1561079311-vJ8lGn6Q-0-628a680d76d8af4c614850467b0153b5'

resp = requests.get(url, headers=headers)
# with open('ting_ting_FM.mp3', 'wb')as f:
#     f.write(resp.content)
print(resp)