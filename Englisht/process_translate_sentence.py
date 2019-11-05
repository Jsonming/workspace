#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 10:56
# @Author  : yangmingming
# @Site    : 
# @File    : process_translate_sentence.py
# @Software: PyCharm
from mylib.redis_my import MyRedis


class ProcessTranslateSentence(object):
    def __init__(self):
        pass

    def process_original_sentence(self):
        """
            处理分析强哥给的原始的句子
        :return:
        """
        mr = MyRedis()
        redis_db_name = "corpus_temp_fingerprint"

        recoding_corpus = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\20W录音语料（带音标）随机\20W录音语料（带音标）随机.txt"
        English_recoding_corpus = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\2500小时英语录音语料（带音标60W）随机\2500小时英语录音语料（带音标60W）随机.txt"

        with open(English_recoding_corpus, 'r', encoding='utf8')as f:
            for line in f:
                sentence = line.split(" 	")[0]
                fingerprint = mr.generate_md5(sentence)
                if not mr.hash_exist(fingerprint):
                    mr.hash_(fingerprint)
                else:
                    print(sentence)

    def process_new_sentence(self):
        """
            处理新抓取的句子
        :return:
        """

    def remove_repeat_sentence(self):
        """
            去重
        :return:
        """

    def output_new_sentence(self):
        """
            输出到文件
        :return:
        """


if __name__ == '__main__':
    pts = ProcessTranslateSentence()
    pts.process_original_sentence()
