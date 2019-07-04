#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 13:46
# @Author  : yangmingming
# @Site    : 
# @File    : lib.py
# @Software: PyCharm
import re
from polyglot.text import Text


def delete_brackets_content(content):
    """
        删除括号中内容
    :param content:
    :return:
    """
    pattern_brackets = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|<.*?>|«.*?»", re.S)
    content = re.sub(pattern_brackets, '', content)
    return content.strip()


def delete_brackets(content):
    """
        删除括号（小括号,大括号,中括号，花括号）
    :param content:
    :return:
    """
    pattern_brackets = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|«|»""")
    content = re.sub(pattern_brackets, '', content)
    return content.strip()


def replace_newline_characters(content, sep=" "):
    """
        替换换行符
    :param content:
    :param sep:
    :return:
    """
    content = content.replace(r"\r\n", sep).replace(r"\n", sep).replace("\r\n", sep).replace("\n", sep)
    return content.strip()


def delete_extra_spaces(content):
    """
        删除多于空格，多个空格合并成一个
    :param content:
    :return:
    """
    patten = re.compile('[\s]+')
    content = re.sub(patten, ' ', content)
    return content.strip()


# 以上是针对文章的处理的函数，一下是针对句子的处理
def split_content(content):
    """
        万国语分隔，将文本内容转化为句子
    :param content:
    :return: 句子列表
    """
    sentences = Text(content).sentences
    sentences = [item.string.strip() for item in sentences if item]
    return sentences


# 汉语切分句子
def chinese_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    para = para.strip()
    return [item.strip() for item in para.split("\n")]


def delete_special_characters(sentence):
    """
        替换句子中的特殊字符
    :param sentence:
    :param sep:
    :return:
    """
    pattern = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|►|▷|◇|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]+|×|™|@|▻|"
                         "～|⁺|⋆|℃|℉|□|ʹ|•|▪|✔|♫", re.S)  # TODO 特殊字符集还需添加
    _sentence = re.sub(pattern, '', sentence)
    return _sentence.strip()


def contain_number(sentence):
    """ 判断是否含有数字"""
    pattern_three = re.compile("[0-9]+", re.S)
    macth = re.findall(pattern_three, sentence)
    return True if macth else False


def sentence_length(sentence):
    """
        计算句子长度句子长度
    :param sentence:
    :return:
    """
    return len(sentence.split())


def count_chinese_length(sentence):
    """
        统计中文字符个数
    :param sentence:
    :return:
    """
    filtate = re.compile('[^\u4E00-\u9FA5]')
    filtered_str = filtate.sub(r'', sentence)
    return len(filtered_str)