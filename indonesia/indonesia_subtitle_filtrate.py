#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 17:37
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_subtitle_filtrate.py
# @Software: PyCharm

import re
import xlwt
import os
from mylib.redis_my import MyRedis

file_name = r'C:\Users\Administrator\Desktop\Indonesian-03-20\Indonesian-03-20.txt'
# file_name = 'indonesia_subtitle_filtrate_text'
dir_name = 'C:\\Users\\Administrator\\Desktop\\indonesia_subtitle\\'

sentence_sum, character_sum = 0, 0
with open(file_name, 'r', encoding='utf8')as f:
    my_redis = MyRedis()
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('content')
    for line in f:
        line_content = re.sub("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|♪|=|“|”|\.+|[0-9]+", "", line)
        line_content = line_content.strip()
        line_length = len(line_content.split())
        if line_length > 6:
            fingerprint = my_redis.generate_md5(line_content)
            if not my_redis.hash_exist(fingerprint):
                my_redis.hash_(fingerprint)
                row = sentence_sum % 10000
                if not row:
                    workbook.save(dir_name + str(sentence_sum // 10000) + '.xls')
                    workbook = xlwt.Workbook(encoding='utf8')
                    worksheet = workbook.add_sheet('content')
                worksheet.write(row, 0, line_content)
                sentence_sum += 1
                character_sum += line_length
                print(sentence_sum)

workbook.save(dir_name + str(sentence_sum // 10000 + 1) + '.xls')
os.remove('C:\\Users\\Administrator\\Desktop\\indonesia_subtitle\\0.xls')
print(sentence_sum, character_sum, character_sum / sentence_sum)
with open('result.txt', 'w', encoding='utf8') as ef:
    f.write(str(character_sum / sentence_sum))