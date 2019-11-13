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


# with open('aaa', 'r', encoding='utf8')as f:
#     data = f.read()


def sentence_filter(paragraph):
    """
        过滤并分割句子
    :param paragraph: 传入段落或者整篇文章
    :return: 返回一个符合的句子列表
    """
    pattern = re.compile(r'\n+')
    match = re.compile(r'[0-9]+|\(|\[')

    result = []
    for sentence in nltk.sent_tokenize(paragraph):
        replace_sentence = re.sub(pattern, ' ', sentence)
        sentence_content = replace_sentence.strip()
        sentence_length = len(sentence_content.split())
        match_result = match.search(sentence_content)
        if 10 <= sentence_length <= 18 and match_result is None:
            result.append(sentence_content)
    return result


def read_data():
    """
        读取content 数据
    :return:
    """
    db = pymysql.connect('123.56.11.156', 'sjtUser', 'sjtUser!1234', 'malaysia')
    cursor = db.cursor(cursor=pymysql.cursors.SSCursor)
    cursor.execute("select content from malaysia.news_content;")
    data = cursor.fetchmany(100)
    while data:
        yield data
        data = cursor.fetchmany(100)


def run():
    sentence_sum, character_sum, essay_num = 0, 0, 0
    dir_name = 'C:\\Users\\Administrator\\Desktop\\news_content\\'
    data = read_data()
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('news_content')
    for lines in data:
        print(essay_num)
        essay_num += 1
        for line in lines:
            if line:
                content = line[0]
                sentence_list = sentence_filter(content)
                for sentence in sentence_list:
                    row = sentence_sum % 10000
                    if not row:
                        workbook.save(dir_name + str(sentence_sum//10000) + '.xls')
                        workbook = xlwt.Workbook(encoding='utf8')
                        worksheet = workbook.add_sheet('news_content')
                    sentence_sum += 1
                    character_sum += len(sentence.split())
                    worksheet.write(row, 0, sentence)
    workbook.save(dir_name + str(sentence_sum//10000 + 1) + '.xls')
    print(sentence_sum, character_sum, character_sum/sentence_sum)


if __name__ == '__main__':
    run()
