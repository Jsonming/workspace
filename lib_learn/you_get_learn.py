#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 23:30
# @Author  : yangmingming
# @Site    : 
# @File    : you_get_learn.py
# @Software: PyCharm

import sys
import you_get


def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


if __name__ == '__main__':
    url = "https://www.bilibili.com/video/av37229426?from=search&seid=7467537021357775133"
    path = "C:\\Users\\Administrator\\Desktop\\"
    download(url, path)
