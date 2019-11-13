#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 15:41
# @Author  : yangmingming
# @Site    :
# @File    : news_sentence_split.py
# @Software: PyCharm
import nltk
import re
import xlwt
import pymysql
from konlpy.tag import Kkma
import os
from polyglot.text import Text


def sentence_filter(paragraph):
    """
        过滤并分割句子
    :param paragraph: 传入段落或者整篇文章
    :return: 返回一个符合的句子列表
    """

    pattern_one = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|►|▷|◇|-|…|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]+|×|&|™|@►|▻|～|⁺|⋆|’|℃|℉", re.S)
    pattern_eight = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
    pattern_zero = re.compile("\\（|\\）|\\{|\\}|\[|\]|【|】|\\(|\\)|\\{|}|\\[|\\]|<|>", re.S)
    pattern_three = re.compile("[a-zA-Z0-9]+|[\u4e00-\u9fa5]+|[\u30a0-\u30ff]+|[\u3040-\u309f]+|/", re.S)
    pattern_specal = re.compile("\'", re.S)

    result = []
    paragraph = paragraph.replace("\n", '').replace("\r", '').replace("\t", '')
    paragraph = paragraph.strip()
    if paragraph:
        sentences = Text(paragraph).sentences
        for sentence in sentences:
            sentence = sentence.string
            sentence = re.sub(pattern_one, '', sentence)
            sentence = re.sub(pattern_eight, '', sentence)
            sentence = re.sub(pattern_zero, '', sentence)
            macth = re.findall(pattern_three, sentence)
            if not macth:
                search = re.findall(pattern_specal, sentence)
                search_result = len(search) % 2
                if not search_result:
                    sentence_content = sentence.strip()
                    sentence_length = len(sentence_content)
                    if 4 < sentence_length:
                        result.append(sentence_content)
    return result


def read_data():
    """
        读取content 数据
    :return:
    """
    db = pymysql.connect('123.56.11.156', 'sjtUser', 'sjtUser!1234', 'malaysia')
    cursor = db.cursor(cursor=pymysql.cursors.SSCursor)
    cursor.execute("select news_text from malaysia.korean_news_text where 10000<id;")
    data = cursor.fetchmany(10)
    while data:
        yield data
        data = cursor.fetchmany(10)


def run():
    sentence_sum, character_sum, essay_num = 0, 0, 0
    dir_name = 'C:\\Users\\Administrator\\Desktop\\korean\\'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    data = read_data()
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('news_content')
    for lines in data:
        for line in lines:
            if line:
                content = line[0]
                sentence_list = sentence_filter(content)
                if sentence_list:
                    for sentence in sentence_list:
                        print(sentence_sum)
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
