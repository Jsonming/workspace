#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 10:19
# @Author  : yangmingming
# @Site    : 
# @File    : malay_lang_split.py
# @Software: PyCharm
import re
import xlwt

file_name = 'Malay.txt'

sentence_sum, character_sum = 0, 0
workbook = xlwt.Workbook(encoding='ascii')
with open(file_name, 'r', encoding='utf8')as f:
    for line in f:
        line_text = line.strip()
        line_length = len(line_text.split())
        if 8 <= line_length <= 15:
            match = re.findall(r'[0-9]', line_text)
            if '('and ')' in line_text:
                match = True
            if not match:
                row = sentence_sum % 10000
                if not row:
                    worksheet = workbook.add_sheet(str(sentence_sum//10000))
                worksheet.write(row, 0, line_text)
                sentence_sum += 1
                character_sum += line_length

worksheet = workbook.add_sheet('sum')
worksheet.write(0, 0, 'sentence_sum')
worksheet.write(0, 1, 'character_sum')
worksheet.write(0, 2, 'character_sentence_average')
worksheet.write(1, 0, str(sentence_sum))
worksheet.write(1, 1, str(character_sum))
worksheet.write(1, 2, str(character_sum/sentence_sum))
workbook.save('malaysia_sub.xls')
