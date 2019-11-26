#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 10:56
# @Author  : yangmingming
# @Site    : 
# @File    : process_translate_sentence.py
# @Software: PyCharm
import nltk
from work.mylib.redis_my import MyRedis, SSDBCon
from work.mylib.mysql_my import MySql
from work.mylib.lib import delete_special_characters, contain_number, sentence_length
from work.dingding.dingding_decorator import dingding_monitor
from work.Englisht.deal_apostrophe import apostrophe_index
from work.mylib.lib import big_file_remove_same


class ProcessTranslateSentence(object):
    def __init__(self):
        with open('简单句单词总.txt', 'r', encoding='utf8') as f:
            self.simple_word = set(f.read().split('\n'))

    @dingding_monitor
    def process_original_sentence(self):
        """
            处理分析强哥给的原始的句子
        :return:
        """
        mr = SSDBCon()
        redis_db_name = "corpus_recording_fingerprint"

        recoding_corpus = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\20W录音语料（带音标）随机\20W录音语料（带音标）随机.txt"
        English_recoding_corpus = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\2500小时英语录音语料（带音标60W）随机\2500小时英语录音语料（带音标60W）随机.txt"

        with open(English_recoding_corpus, 'r', encoding='utf8')as f:
            for line in f:
                sentence = line.split("\t")[0]
                if not mr.exist_finger(redis_db_name, sentence):
                    mr.insert_finger(redis_db_name, sentence)

    def read_data(self, start=1):
        my = MySql()
        sql = """select * from spiderframe.translate_sentence_new where id >10;"""
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

    @dingding_monitor
    def process_new_sentence(self):
        """
            处理抓取的句子
        :return:    将抓取的句子分类后输出到本地文件
        """
        with open('not_contain_num.txt', 'a', encoding='utf8') as \
                not_num_f, open("contain_num.txt", 'a', encoding='utf8') as num_f:

            for batch in self.read_data():
                for row in batch:
                    sentence = row[4]
                    sentence = delete_special_characters(sentence)
                    sentence = sentence.replace('"', '')
                    sentence_len = sentence_length(sentence)
                    sentence = sentence.strip()
                    sentence = sentence.capitalize()
                    if 1 < sentence_len:
                        if not contain_number(sentence):
                            words = nltk.word_tokenize(sentence)
                            word_index = apostrophe_index(words)
                            if not word_index:
                                not_num_f.write(sentence + "\n")
                        else:
                            num_f.write(sentence + "\n")

    @dingding_monitor
    def remove_repeat_sentence(self):
        """
            去重
        :return:
        """
        mr = MyRedis()

        remove_before_file = "news_num_sentence_temp.txt"
        remove_after_file = "news_num_sentence_new.txt"

        with open(remove_before_file, 'r', encoding='utf8')as f, \
                open(remove_after_file, 'a', encoding='utf8') as new_f:

            for line in f:
                sentence = line.strip()
                fingerprint = mr.generate_md5(sentence)
                if not mr.hash_exist(fingerprint):
                    new_f.write(sentence + "\n")
                    mr.hash_(fingerprint)
                else:
                    print(sentence)

    @dingding_monitor
    def same_sentence(self):
        """
            输出到文件
        :return:
        """
        from work.mylib.lib import big_file_remove_same
        big_file_remove_same("news_num_sentence.txt", "news_num_sentence_temp.txt")


if __name__ == '__main__':
    pts = ProcessTranslateSentence()
    pts.process_original_sentence()
