#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 14:49
# @Author  : yangmingming
# @Site    : 
# @File    : count_senten_length.py
# @Software: PyCharm
import json
from collections import Counter
import pandas as pd

from operator import itemgetter
from mylib.lib import list_file



class CountSentenceLength(object):
    def __init__(self):
        pass

    def count_sentence_length(self, file):
        sentences = []
        with open(file, 'r', encoding='utf')as f:
            for line in f:
                line = line.replace("#1", '').replace("#2", '').replace("#3", '').replace("#4", '').strip()
                if len(line) < 14 or 35 < len(line):
                    sentences.append(line)
        return sentences

    def run(self, path):
        files = list_file(path)
        length_list = []
        info = []
        for file in files:
            if file.endswith('txt'):
                # length = self.count_sentence_length(file)
                # length_list.extend(length)

                sentences = self.count_sentence_length(file)
                for sentence in sentences:
                    info.append({"file_name": file, "sentence": sentence, "length": len(sentence)})

        pf = pd.DataFrame(info)
        pf.to_excel("ab_sentence.xlsx", index=False)
        # counter = Counter()
        # for l in length_list:
        #     counter[l] += 1
        #
        # info = sorted(counter.items(), key=itemgetter(0))
        # pf = pd.DataFrame(info)
        # pf.to_excel('sentence_length.xlsx', index=False)


if __name__ == '__main__':
    folder = r'\\10.10.8.123\20万句中文韵律文本标注\交付数据'
    csl = CountSentenceLength()
    csl.run(folder)
