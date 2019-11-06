#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 10:56
# @Author  : yangmingming
# @Site    : 
# @File    : process_translate_sentence.py
# @Software: PyCharm
from mylib.redis_my import MyRedis
from mylib.mysql_my import MySql
from mylib.lib import delete_special_characters, contain_number, sentence_length
import nltk


class ProcessTranslateSentence(object):
    def __init__(self):
        with open('简单句单词总.txt', 'r', encoding='utf8') as f:
            self.simple_word = set(f.read().split('\n'))

    def process_original_sentence(self):
        """
            处理分析强哥给的原始的句子
        :return:
        """
        mr = MyRedis()
        redis_db_name = "corpus_temp_fingerprint"

        recoding_corpus = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\20W录音语料（带音标）随机\20W录音语料（带音标）随机.txt"
        English_recoding_corpus = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\2500小时英语录音语料（带音标60W）随机\2500小时英语录音语料（带音标60W）随机.txt"

        with open(recoding_corpus, 'r', encoding='utf8')as f:
            for line in f:
                sentence = line.split("\t")[0]
                fingerprint = mr.generate_md5(sentence)
                if not mr.hash_exist(fingerprint):
                    mr.hash_(fingerprint)

    def read_data(self, start=1):
        my = MySql()
        sql = """select * from spiderframe.translate_sentence where id > 2000;"""
        return my.get_many(sql)

    def contain_word(self, words):
        """
            判断单词包含
        :param sentence:
        :return:
        """
        special_char = ["?", ",", ".", "!", "'", "'m", "'d", "'re", "n't", "'s", "'ll", "'ve"]
        flag = [True if word.lower() in self.simple_word or word.lower() in special_char else False for word in words]
        return all(flag)

    def process_new_sentence(self):
        """
            处理新抓取的句子
        :return:    将抓取的句子分类后输出到本地文件
        """
        with open('not_contain_num.txt', 'a', encoding='utf8') as not_num_f, open("contain_num.txt", 'a',
                                                                                  encoding='utf8') as num_f:

            for batch in self.read_data():
                for row in batch:
                    sentence = row[4]
                    sentence = delete_special_characters(sentence)
                    sentence = sentence.replace('"', '')
                    sentence_len = sentence_length(sentence)
                    if 1 < sentence_len:
                        if not contain_number(sentence):
                            words = nltk.word_tokenize(sentence)
                            if self.contain_word(words):
                                not_num_f.write(sentence + "\n")
                        else:
                            num_f.write(sentence + "\n")

    def remove_repeat_sentence(self):
        """
            去重
        :return:
        """
        mr = MyRedis()

        remove_before_file = "not_contain_num.txt"
        remove_after_file = "simple_sentence.txt"

        with open(remove_before_file, 'r', encoding='utf8')as f, open(remove_after_file, 'a', encoding='utf8') as new_f:
            for line in f:
                sentence = line.strip()
                fingerprint = mr.generate_md5(sentence)
                if not mr.hash_exist(fingerprint):
                    mr.hash_(fingerprint)
                    # new_f.write(sentence + "\n")

    def output_new_sentence(self):
        """
            输出到文件
        :return:
        """


if __name__ == '__main__':
    pts = ProcessTranslateSentence()
    pts.remove_repeat_sentence()
