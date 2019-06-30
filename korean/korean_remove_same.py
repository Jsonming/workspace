#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 10:51
# @Author  : yangmingming
# @Site    : 
# @File    : korean_remove_same.py
# @Software: PyCharm
import xlrd
import xlwt
import hashlib
from mylib.move_file import list_file
import os
import pandas as pd

# file_name = r"D:\datatang\workspace\korean\korean_subtitle\subtitle.xls"
# dir_name = r"D:\datatang\workspace\korean\korean_subtitle\data"
#
# sentence_sum, character_sum, essay_num = 0, 0, 0
# fingerprint = set()
#
# workbook2 = xlwt.Workbook(encoding='utf8')
# worksheet2 = workbook2.add_sheet('subtitle_content')
#
# workbook = xlrd.open_workbook(file_name)
# worksheets = workbook.sheets()
# for worksheet in worksheets:
#     sentences = worksheet.col_values(0)
#     for sentence in sentences:
#         md5_value = hashlib.md5(sentence.encode('utf8')).hexdigest()
#         if md5_value not in fingerprint:
#             fingerprint.add(md5_value)
#             sentence_length = len(sentence.replace(" ", ''))
#
#             row = sentence_sum % 10000
#             if not row:
#                 workbook2.save(dir_name + str(sentence_sum // 10000) + '.xls')
#                 workbook2 = xlwt.Workbook(encoding='utf8')
#                 worksheet2 = workbook2.add_sheet('subtitle_content')
# sentence_sum += 1
# character_sum += sentence_length
# worksheet2.write(row, 0, sentence)
# workbook2.save(dir_name + str(sentence_sum // 10000 + 1) + '.xls')
# print(sentence_sum, character_sum, character_sum / sentence_sum)


folder = r"C:\Users\Administrator\Desktop\korean"
folder_old = r"C:\Users\Administrator\Desktop\work_temp\korean_news_data_new\korean_news_data_new"
to_folder = r"C:\Users\Administrator\Desktop\korean_new"
if not os.path.exists(to_folder):
    os.mkdir(to_folder)


def get_data(folder):
    new_data = list()
    sum_sent = 0
    cont = []
    file_list = list_file(folder=folder)
    for file in file_list:
        workbook = xlrd.open_workbook(file)
        worksheet = workbook.sheets()[0]
        sentence_list = worksheet.col_values(0)
        for sentence in sentence_list:
            sentence_length = len(sentence.replace(" ", ''))
            cont.append(sentence_length)
            if 14 < sentence_length < 36:
                new_data.append(sentence)
                sum_sent += sentence_length
    return new_data


new_data = get_data(folder)
new_data = set(new_data)
old_data = get_data(folder_old)
old_data = set(old_data)

data = list(new_data - old_data)

data_split_group = [data[i: i + 10000] for i in range(0, len(data), 10000)]
for index, data_unit in enumerate(data_split_group):
    data_unit = [item.strip() for item in data_unit]
    df = pd.DataFrame(data_unit)
    df.to_excel('{}/{}.xls'.format(to_folder, str(index)), header=False, index=False)
