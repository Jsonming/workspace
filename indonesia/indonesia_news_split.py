#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 9:40
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_news_split.py
# @Software: PyCharm

import nltk
import re
import xlwt
import pymysql
from polyglot.text import Text


def sentence_filter(paragraph):
    """
        过滤并分割句子
    :param paragraph: 传入段落或者整篇文章
    :return: 返回一个符合的句子列表
    """

    pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|"
                         "[0-9]+|♪|=|※|●|■|~|▶|▲|☞|▷|◇|…|○|#|◆|\//+|\/|[①②③④⑤⑥⑦⑧]+|×|&", re.S)
    pattern_new = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|'|“|”|‘|’""")

    result = []
    paragraph = paragraph.replace("\n", ' ').replace("\t", '')
    paragraph = paragraph.strip()
    if paragraph:
        sentences = Text(paragraph).sentences
        for sentence in sentences:
            sentence = re.sub(pattern, '', sentence.string)
            sentence = re.sub(pattern_new, '', sentence)
            sentence = ' '.join(filter(lambda x: x, sentence.split(' ')))
            sentence_content = sentence.strip()
            sentence_length = len(sentence_content.split())
            if 8 <= sentence_length <= 16:
                result.append(sentence_content)
    return result


def read_data():
    """
        读取content 数据
    :return:
    """
    db = pymysql.connect('123.56.11.156', 'sjtUser', 'sjtUser!1234', 'malaysia')
    cursor = db.cursor(cursor=pymysql.cursors.SSCursor)
    cursor.execute("select news_text from malaysia.indonesia_news_text;")
    data = cursor.fetchmany(100)
    while data:
        yield data
        data = cursor.fetchmany(100)


def run():
    sentence_sum, character_sum, essay_num = 0, 0, 0
    dir_name = 'C:\\Users\\Administrator\\Desktop\\indonesia_old\\'
    data = read_data()
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('news_content')
    for lines in data:
        essay_num += 1
        print(essay_num)
        for line in lines:
            if line:
                content = line[0]
                sentence_list = sentence_filter(content)
                for sentence in sentence_list:
                    if sentence:
                        row = sentence_sum % 10000
                        if not row:
                            workbook.save(dir_name + str(sentence_sum // 10000) + '.xls')
                            workbook = xlwt.Workbook(encoding='utf8')
                            worksheet = workbook.add_sheet('news_content')
                        sentence_sum += 1
                        character_sum += len(sentence.split())
                        worksheet.write(row, 0, sentence)
    workbook.save(dir_name + str(sentence_sum // 10000 + 1) + '.xls')
    print(sentence_sum, character_sum, character_sum / sentence_sum)


if __name__ == '__main__':
    run()
