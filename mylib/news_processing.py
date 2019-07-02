#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 16:58
# @Author  : yangmingming
# @Site    : 
# @File    : news_processing.py
# @Software: PyCharm
import re

from mylib.mysql_my import MySql
from polyglot.text import Text
import pandas as pd
import numpy as np
import json
import time
from collections import defaultdict


class NewProcess(object):
    def __init__(self):
        self.sentence_limit_length = (10, 26)
        self.result = []
        self.word = defaultdict(int)
        self.legal_char = set()
        self.elem_type = set(["thoi-su", "kinh-doanh", "the-thao", "giai-tri"])

    def read_execl(self, file):
        """ 读execl"""
        data = pd.read_excel(file, sheet_name="news_content")
        data = np.array(data).tolist()
        data = [item[0] for item in data]
        return data

    def read_txt(self, file):
        with open(file, 'r', encoding='utf8')as f:
            data = f.readlines()
            data = [item.strip() for item in data]
        return data

    def read_data(self):
        """
            get data in the form of a generator, each element containing the number of data see mysql_my,py
        :return: generator
        """
        sql = 'select url, content from spiderframe.vietnam_news_vn_content where 300000<id < 400000;'
        my_mysql = MySql()
        data = my_mysql.get_many(sql)
        return data

    def remove_specal_char(self, content):
        pattern_one = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|►|▷|◇|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]+"
                                 "|×|™|@►|▻|～|⁺|⋆|℃|℉|□|ʹ|•|▪|✔|♫",
                                 re.S)
        content = re.sub(pattern_one, '', content)
        pattern_two = re.compile("_")
        content = re.sub(pattern_two, ' ', content)
        return content

    def remove_branck(self, content):
        pattern_eight = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|<.*?>|«.*?»", re.S)
        pattern_two = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|“|”|’|‘|«|»""")
        content = re.sub(pattern_eight, '', content)
        content = re.sub(pattern_two, '', content)
        return content.strip()

    def remove_spaces(self, content):
        content = content.replace("\n", ' ').replace("\t", '').replace("\r", '')
        patten = re.compile('[\s]+')
        content = re.sub(patten, ' ', content)
        return content

    def deal_content(self, content):
        content = self.remove_spaces(content)
        return content.strip()

    def sentence_length(self, sentence):
        """ 句子长度"""
        sentence_length = len(sentence.split())
        return sentence_length

    def deal_with_by_author(self, sentence):
        """  留给用户自己处理数据"""
        # 印尼
        # 删掉含有不合法标点符号的句子
        # pattern_nine = re.compile(
        #     "[\u0060|\u0021-\u002c|\u002e-\u002f|\u003a-\u003f|\u2200-\u22ff|\uFB00-\uFFFD|\u2E80-\u33FF]")
        # punctuation = set(re.findall(pattern_nine, sentence))
        # leg_punctuation = set(""";,-!.?"'""")
        # remain = punctuation - leg_punctuation
        # if remain:
        #     sentence = ""
        # 删除含有不是英文字母与合法标点的句子, 同时合并多于空格
        # pattern = re.compile("""[a-zA-Z;,\-!\.?"']+""")
        # char = re.findall(pattern, sentence)
        # if char:
        #     sentence = ' '.join([char[0].capitalize()] + char[1:])
        # mark_length = len(re.findall("""['"]+""", sentence))
        # if mark_length % 2:
        #     sentence = ''

        # 越南语
        pattern_nine = re.compile(
            "[\u0060|\u0021-\u002c|\u002e-\u002f|\u003a-\u003f|\u2200-\u22ff|\uFB00-\uFFFD|\u2E80-\u33FF]")
        punctuation = set(re.findall(pattern_nine, sentence))
        leg_punctuation = set(""":,-\.!?？；！-:,–-.!?？；！… ·""")
        remain = punctuation - leg_punctuation
        if remain:
            sentence = ""
        sentence_set = set(sentence)
        legal_set = self.legal_char | leg_punctuation
        if not sentence_set.issubset(legal_set):
            sentence = ""
        return sentence

    def deal_with_sentence(self, sentence):
        """ 通用处理句子, 删除特殊字符, 删除括号内容, 含有数字的直接不要了"""
        sentence = self.remove_specal_char(sentence)
        sentence = self.remove_branck(sentence)
        if self.contain_number(sentence):
            sentence = ''
        return sentence

    def contain_number(self, sentence):
        """ 含有数字"""
        pattern_three = re.compile("[0-9]+", re.S)
        macth = re.findall(pattern_three, sentence)
        if macth:
            return True
        else:
            return False

    def split_sentence(self, content):
        sentences = Text(content).sentences
        sentences = [item.string for item in sentences]
        # sentences = []
        # for line in content.split('.'):
        #     for lin in line.split('?'):
        #         for word in lin.split("!"):
        #             sentences.append(word)
        return sentences

    def deal_with_data(self, data):
        for batch in data:
            for element in batch:
                url = element[0]
                try:
                    element_type = url.split("/")[3]
                except:
                    element_type = ""

                if element_type in self.elem_type:
                    news_content = element[1]
                    news_content = news_content.strip()
                    if news_content:
                        content_new = self.deal_content(news_content)
                        sentences = self.split_sentence(content_new)
                        for sentence in sentences:
                            sentence = self.deal_with_sentence(sentence)
                            sentence = self.deal_with_by_author(sentence)
                            sentence_len = self.sentence_length(sentence)
                            if self.sentence_limit_length[0] <= sentence_len < self.sentence_limit_length[1]:
                                # self.result.append(sentence)
                                file = r"C:\Users\Administrator\Desktop\vietnam_news_vn.txt"
                                with open(file, 'a', encoding='utf8')as f:
                                    f.write(sentence + '\n')

    def save_txt(self, file, result):
        with open(file, 'a', encoding='utf8')as f:
            f.write('\n'.join(result))

    def save_excel(self, file, result):
        result = list(set(result))
        df = pd.DataFrame(result)
        df.to_excel(file, index=False, header=False)

    def run(self):
        """
            Main control logic
        :return:
        """

        file = r"C:\Users\Administrator\Desktop\vietnam_news_content.txt"
        vietnam_charater = "aăâbcdđeêfghijklmnoôơpqrstuwưvxyzAĂÂBCDĐEÊFGHIJKLMNOÔƠPQRSTUƯVWXYZàằầèềìòồờùừỳÀẰẦÈỀÌÒỒỜÙỪỲáắấéế" \
                           "íóốớúứýÁẮẤÉẾÍÓỐỚÚỨÝảẳẩẻểỉỏổởủửỷẢẲẨẺỂỈỎỔỞỦỬỶãẵẫẽễĩõỗỡũüữỹÃẴẪẼỄĨÕỖỠŨỮỸạặậẹệịọộợụự" \
                           "ỵẠẶẬẸỆỊỌỘỢỤỰỴÞðśłΚäöÐïøñ"
        self.legal_char = set(vietnam_charater)
        data = self.read_data()
        self.deal_with_data(data)
        # self.save_txt(file, self.result)

        # with open(r"C:\Users\Administrator\Desktop\temp.txt", 'r', encoding='utf8') as sentences:
        #     for sentence in sentences:
        #         sentence = self.deal_content(sentence)
        #         sentence = sentence.strip()
        #         sentence = self.deal_with_sentence(sentence)
        #         sentence = self.deal_with_by_author(sentence)
        #         sentence_len = self.sentence_length(sentence)
        #         if self.sentence_limit_length[0] <= sentence_len < self.sentence_limit_length[1]:
        #             self.result.append(sentence)
        #             file = r"C:\Users\Administrator\Desktop\vietnam_speaking.txt"
        #             with open(file, 'a', encoding='utf8')as f:
        #                 f.write(sentence + '\n')


if __name__ == '__main__':
    news = NewProcess()
    news.run()
