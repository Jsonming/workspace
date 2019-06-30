#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 17:21
# @Author  : yangmingming
# @Site    :
# @File    : vietnam_short_word_filter.py
# @Software: PyCharm
import re
import pandas as pd


def remove_same(data):
    data = list(set(data))
    return data


def read_data(file):
    with open(file, 'r', encoding='utf8')as f:
        data = f.readlines()
        data = [item.strip() for item in data]
        data = [item for item in data if item]
    return data


def run(file):
    parttern = re.compile(">|-|“”")
    new_data, result = [], []
    data = read_data(file)
    for word in data:
        new_data.extend(word.split(';'))
    for new_word in new_data:
        new_word = new_word.strip()
        if not re.findall(parttern, new_word):
            if not new_word.endswith(":"):
                if 2 < len(new_word):
                    result.append(new_word)
    result = list(set(result))
    print(len(result))
    pf = pd.DataFrame(result)
    pf.to_excel(r'C:\Users\Administrator\Desktop\vietnam\short_word.xls', header=False, index=False)


if __name__ == '__main__':
    file = r"C:\Users\Administrator\Desktop\short_word.txt"
    run(file)
