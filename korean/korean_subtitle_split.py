#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:09
# @Author  : yangmingming
# @Site    : 
# @File    : korean_subtitle_split.py
# @Software: PyCharm
import os
import chardet
import re
import xlwt

home_folder = r"D:\datatang\workspace\korean\korean_subtitle"
pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
pattern_one = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|▷|◇|-|…|○|#|◆|⚽|♬|\*|\//+|\/|[①②③④⑤⑥⑦⑧]+|×|&|nbsp;|™|@", re.S)
pattern_two = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|'|“|”|‘|’|,|;|；|:|'|∼|\.""")
pattern_three = re.compile("[a-zA-Z0-9]+", re.S)

workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('content')
sentence_sum, character_sum, essay_num = 0, 0, 0

for sub_folder in os.listdir(home_folder):
    sub_folder_path = os.path.join(home_folder, sub_folder)
    if os.path.isdir(sub_folder_path):
        for file in os.listdir(sub_folder_path):
            file_path = os.path.join(sub_folder_path, file)
            print(file_path)
            f = open(file_path, 'rb')
            data = f.read()
            code_type = chardet.detect(data).get("encoding")
            if code_type == "utf-8":
                ff = open(file_path, 'r', encoding='utf8')
            elif code_type == "CP949":
                ff = open(file_path, 'r', encoding='CP949')
            elif code_type == "EUC-KR":
                ff = open(file_path, 'r', encoding='EUC-KR')
            elif code_type == "UTF-8-SIG":
                ff = open(file_path, 'r', encoding='UTF-8-SIG')
            print("*"*100)
            sentence = ff.read()
            # print(sentence)
            sentence = re.sub(pattern, '', sentence)
            sentence = re.sub(pattern_one, '', sentence)
            sentence = re.sub(pattern_two, '', sentence)
            sentence = re.sub(pattern_three, '', sentence)
            sentence = ' '.join(filter(lambda x: x, sentence.split(' ')))
            for line in sentence.split("\n"):
                line_string = line.strip()
                if line_string:
                    print(line_string)
                    row = sentence_sum % 10000
                    if not row:
                        worksheet = workbook.add_sheet(str(sentence_sum//10000))
                    sentence_sum += 1
                    worksheet.write(row, 0, line_string)
workbook.save(home_folder + r"\subtitle.xls")