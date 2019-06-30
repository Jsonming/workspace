#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 9:12
# @Author  : yangmingming
# @Site    : 
# @File    : korean_static.py
# @Software: PyCharm
import os
import xlrd
import xlwt

home_folder = "D:\datatang\workspace\korean\korean_news_data\\"
dir_name = "D:\datatang\workspace\korean\korean_news_data_new\\"
workbook2 = xlwt.Workbook(encoding='utf8')
worksheet2 = workbook2.add_sheet('news_content')

sentence_sum = 0
character_sum = 0

for file_name in os.listdir(home_folder):
    file_path = home_folder + file_name
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheets()[0]
    sentences = worksheet.col_values(0)
    for sentence in sentences:
        sentence_length = len(sentence.replace(" ", ''))
        if 15 < sentence_length < 35:
            row = sentence_sum % 10000
            if not row:
                workbook2.save(dir_name + str(sentence_sum // 10000) + '.xls')
                workbook2 = xlwt.Workbook(encoding='utf8')
                worksheet2 = workbook2.add_sheet('news_content')
            sentence_sum += 1
            character_sum += sentence_length
            worksheet2.write(row, 0, sentence)
workbook2.save(dir_name + str(sentence_sum // 10000 + 1) + '.xls')

print(sentence_sum, character_sum, character_sum/sentence_sum)