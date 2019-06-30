#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 17:30
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_data_process.py
# @Software: PyCharm
import re
import pandas as pd

input_files = [
    # r"C:\Users\Administrator\Desktop\indonesia_temp\indonesia_short_word_one.txt",
    # r"C:\Users\Administrator\Desktop\indonesia_temp\indonesia_short_word_two.txt",
    # r"C:\Users\Administrator\Desktop\indonesia_temp\indonesia_sights_name_one.txt",
    r"C:\Users\Administrator\Desktop\indonesia_temp\movie_name_two.txt"
]
output_file = r"C:\Users\Administrator\Desktop\indonesia\indonesia_movie_name_.xls"

pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
pattern_one = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|►|▷|◇|…|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]\+|×|&|™|@►|▻|～|⁺|⋆|’|📖|®|🐬﻿",
                         re.S)
pattern_two = re.compile("[0-9]+|I")
fingerprint = set()
names = []

for input_file in input_files:
    with open(input_file, 'r', encoding='utf8') as f:
        for name in f:
            name = name.strip()
            name = name.split('–')[0]
            name = name.split('—')[0]
            name = name.split('-')[0]
            name = name.split('&')[0]
            name = name.split(':')[0]
            name = name.split('|')[0]
            name = name.split('/')[-1]
            name = name.replace('.', '')
            name = re.sub(pattern, '', name)
            match = re.search(pattern_one, name)
            if not match:
                match_two = re.search(pattern_two, name)
                if not match_two:
                    name = name.strip()
                    if name not in fingerprint:
                        if 50 > len(name) > 3:
                            fingerprint.add(name)
                            names.append(name)
                            print(name)

df = pd.DataFrame(names)
df.to_excel(output_file, header=False, index=False)
