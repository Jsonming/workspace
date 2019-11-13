#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 16:31
# @Author  : yangmingming
# @Site    : 
# @File    : korean_sentence_remove.py
# @Software: PyCharm

import xlrd
import xlwt
import hashlib
import os
import re

file_name = 'C:\\Users\\Administrator\\Desktop\\korean\\'
dir_name = 'korean_news_data\\'

sentence_sum, character_sum, essay_num = 0, 0, 0
fingerprint = set()

pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|"
                     "[a-zA-Z0-9]+|♪|=|※|●|■|~|▶|▲|▼|☞|▷|◇|-|…|○|#|◆|⚽|♬|\*|\//+|\/|[①②③④⑤⑥⑦⑧]+|×|&", re.S)
pattern_new = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|'|“|”|‘|’|;|；|:|'|∼|\.""")

workbook2 = xlwt.Workbook(encoding='utf8')
worksheet2 = workbook2.add_sheet('news_content')

for file in os.listdir(file_name):
    file_ = file_name + file
    workbook = xlrd.open_workbook(file_)
    worksheet = workbook.sheets()[0]
    sentences = worksheet.col_values(0)
    for sentence in sentences:
        sentence = re.sub(pattern, '', sentence)
        sentence = re.sub(pattern_new, '', sentence)
        sentence = ' '.join(filter(lambda x: x, sentence.split(' ')))
        sentence = sentence.strip()
        sentence_length = len(sentence.replace(" ", ""))
        if 4 < sentence_length:
            md5_value = hashlib.md5(sentence.encode('utf8')).hexdigest()
            if md5_value not in fingerprint:
                fingerprint.add(md5_value)
                row = sentence_sum % 10000
                if not row:
                    workbook2.save(dir_name + str(sentence_sum // 10000) + '.xls')
                    workbook2 = xlwt.Workbook(encoding='utf8')
                    worksheet2 = workbook2.add_sheet('news_content')
                sentence_sum += 1
                character_sum += sentence_length
                worksheet2.write(row, 0, sentence)
workbook2.save(dir_name + str(sentence_sum // 10000 + 1) + '.xls')
print(sentence_sum, character_sum, character_sum / sentence_sum)

