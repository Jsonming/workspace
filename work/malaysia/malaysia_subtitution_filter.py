#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 15:40
# @Author  : yangmingming
# @Site    : 
# @File    : malaysia_subtitution_filter.py
# @Software: PyCharm
import re
import pandas as pd

path = r"C:\Users\Administrator\Desktop\malaya_temp\singht_name.txt"
file_name = r"C:\Users\Administrator\Desktop\malaysia\singht_name.txt"

with open(path, 'r', encoding='utf8')as f:
    data = f.readlines()
    data = [item.strip() for item in data]
pattern_zero = re.compile("\.|\‘|\’|\'|\+|%|\"|", re.S)
data = [re.sub(pattern_zero, '', item) for item in data]

pattern_one = re.compile("♪|=|※|●|■|⬛|~|▶|▲|▼|☞|►|▷|◇|-|…|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]+|×|&|™|@|\*|▻|～|⁺|⋆|﻿|℃|℉|♥|★",
                         re.S)
data = [re.sub(pattern_one, '', item) for item in data]

pattern_three = re.compile("[0-9]+", re.S)
data = [re.sub(pattern_three, '', item) for item in data]

pattern_eight = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
data = [re.sub(pattern_eight, '', item) for item in data]

data = [item.strip() for item in data]
data = [item for item in data if item]
data = list(set(data))

data_name = []
for name in data:
    pattern_four = re.compile("[\u4e00-\u9fa5]+|[\u30a0-\u30ff]+|[\u3040-\u309f]+", re.S)  # 中文
    match = re.findall(pattern_four, name)
    if not match:
        name = name.split("/")[-1]
        name = name.split("-")[-1]
        name = name.split("|")[-1]
        name = name.split(":")[-1]
        name = name.strip()
        data_name.append(name)
        print(name)

data_name = list(set(data_name))
print(len(data_name))

file_name = file_name.replace('txt', 'xls')
pf = pd.DataFrame(data_name)
pf.to_excel(file_name, header=False, index=False)
