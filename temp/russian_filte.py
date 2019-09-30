#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 11:16
# @Author  : yangmingming
# @Site    : 
# @File    : russian_filte.py
# @Software: PyCharm
from polyglot.text import Text


class RussianFilter(object):
    """
        俄语长句子分隔
    """

    def __init__(self):
        pass

    def read_text(self, file_path):
        with open(file_path, 'r', encoding='utf8')as f:
            for content in f:
                yield content

    def break_up_text(self, content):
        with open(r'C:\Users\Administrator\Desktop\Russian_content.txt', 'a', encoding='utf8')as f:
            sentences = Text(content).sentences
            sentences = [item.string for item in sentences]
            for sentence in sentences:
                f.write(sentence + "\n")

    def run(self):
        file_path = r"C:\Users\Administrator\Desktop\俄语长句子.txt"
        contents = self.read_text(file_path)
        for content in contents:
            self.break_up_text(content)


if __name__ == '__main__':
    rf = RussianFilter()
    rf.run()
