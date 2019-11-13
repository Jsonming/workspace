#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 11:09
# @Author  : yangmingming
# @Site    : 
# @File    : 163_FM.py
# @Software: PyCharm
import requests

headers = {
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Origin': 'https://music.163.com',
    'Range': 'bytes=0-',
    'Referer': 'https://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

url = 'https://m10.music.126.net/20190611185116/7bde3cecfdb01082f81e85cb922eb511/yyaac/0509/060b/565c/2c3adff7c11a4540ba62a651df894b16.m4a'

resp = requests.get(url, headers=headers)
with open('163_FM.mp3', 'wb')as f:
    f.write(resp.content)
print(resp)
