#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 15:41
# @Author  : yangmingming
# @Site    : 
# @File    : tem.py
# @Software: PyCharm
import json
from pprint import pprint
from pymediainfo import MediaInfo

media_info = MediaInfo.parse(r'E:\学习用临时目录\American\1\Bill Gates Chats with Ellen for the First Time.webm')
data = media_info.to_json()
pprint(json.loads(data))