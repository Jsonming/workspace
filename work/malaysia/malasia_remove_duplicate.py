#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 19:15
# @Author  : yangmingming
# @Site    :
# @File    : malasia_remove_same.py
# @Software: PyCharm
import xlrd
import xlwt
import hashlib
import os

# 字幕去重
# file_name = 'C:\\Users\\Administrator\\Desktop\\malaysia_sub.xls'
# dir_name = 'C:\\Users\\Administrator\\Desktop\\subtitle_content\\'
# 新闻去重
old_file = 'C:\\Users\\Administrator\\Desktop\\马来新闻 待去重\\'
dir_name = 'C:\\Users\\Administrator\\Desktop\\new_news_content\\'

sentence_sum, character_sum, essay_num = 0, 0, 0
fingerprint = set()

workbook2 = xlwt.Workbook(encoding='utf8')
worksheet2 = workbook2.add_sheet('news_content')
file_list = os.listdir(old_file)
for file in file_list:
    file_name = old_file + file
    workbook = xlrd.open_workbook(file_name)
    worksheets = workbook.sheets()
    for worksheet in worksheets:
        sentences = worksheet.col_values(0)
        for sentence in sentences:
            md5_value = hashlib.md5(sentence.encode('utf8')).hexdigest()
            if md5_value not in fingerprint:
                print(len(fingerprint))
                fingerprint.add(md5_value)
                row = sentence_sum % 10000
                if not row:
                    workbook2.save(dir_name + str(sentence_sum // 10000) + '.xls')
                    workbook2 = xlwt.Workbook(encoding='utf8')
                    worksheet2 = workbook2.add_sheet('news_content')
                sentence_sum += 1
                character_sum += len(sentence.split())
                worksheet2.write(row, 0, sentence)
workbook2.save(dir_name + str(sentence_sum // 10000 + 1) + '.xls')
print(sentence_sum, character_sum, character_sum / sentence_sum)
