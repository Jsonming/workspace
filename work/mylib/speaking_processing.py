#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 15:55
# @Author  : yangmingming
# @Site    : 
# @File    : speaking_processing.py
# @Software: PyCharm
from work.mylib import NewProcess
import re


class SpeakProcess(object):
    def __init__(self):
        self.result = []

    def deal_with(self, sentence):
        partten = re.compile("♪|=|“|”|[\.]+")
        sentence = re.sub(partten, '', sentence)
        return sentence

    def run(self):
        """ 主逻辑控制"""
        file = r"C:\Users\Administrator\Desktop\Indonesian-03-20\Indonesian-03-20.txt"
        news = NewProcess()
        data = news.read_txt(file)
        for sentence in data:
            sentence = news.deal_content(sentence)
            sentence = self.deal_with(sentence)
            if not news.contain_number(sentence) and 6 < news.sentence_length(sentence):
                sentence = sentence.strip()
                self.result.append(sentence)

        file_2 = r"C:\Users\Administrator\Desktop\indonesia\indonesia_speaking.txt"
        news.save_txt(file_2, self.result)


if __name__ == '__main__':
    speak = SpeakProcess()
    speak.run()
