#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 10:20
# @Author  : yangmingming
# @Site    : 
# @File    : language_split.py
# @Software: PyCharm
from polyglot.detect import Detector

from mylib.txt_to_execl import save_txt


def recognition_language(line):
    try:
        language = Detector(line)
    except:
        print(line)
    else:
        return language.language.name


def language_filter(file, file_new, language):
    data = []
    with open(file, 'r', encoding='utf8') as f:
        for goods_name in f:
            name = goods_name.strip()
            language_class = recognition_language(name)
            if language_class == language:
                data.append(name)
    save_txt(data, file_new)


if __name__ == '__main__':
    file = r"C:\Users\Administrator\Desktop\malaysia_third\gooda_name.txt"
    file_new = r"C:\Users\Administrator\Desktop\malaysia_third\gooda_name.txt"
    language = "马来语"
    language_filter(file, file_new, language)
