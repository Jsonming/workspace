#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 13:46
# @Author  : yangmingming
# @Site    : 
# @File    : lib.py
# @Software: PyCharm
import re
import shutil
import os
import hashlib
from polyglot.text import Text
from unrar import rarfile


def delete_url_link(content):
    pattern_url = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    pattern_url_two = re.compile(r'www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    content = re.sub(pattern_url, ' ', content)
    content = re.sub(pattern_url_two, ' ', content)
    return content


def delete_brackets_content(content):
    """
        删除括号中内容
    :param content:
    :return:
    """
    pattern_brackets = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|<.*?>|«.*?»", re.S)
    content = re.sub(pattern_brackets, ' ', content)
    return content.strip()


def delete_brackets(content):
    """
        删除括号（小括号,大括号,中括号，花括号）
    :param content:
    :return:
    """
    pattern_brackets = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|«|»""")
    content = re.sub(pattern_brackets, ' ', content)
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


def split_content_custom(content):
    """
        自定义句子切分
    :param content:
    :return:
    """
    start = 0
    sentences = []
    split_char = {'.', '?', "!"}
    for i, char in enumerate(content):
        if char in split_char:
            sentences.append(content[start:i + 1])
            start = i + 1
    return sentences


def chinese_sent(para):
    """
        汉语切分句子
    :param para:
    :return:
    """
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
    err_symbol = set()
    with open('../mylib/err_symbol.txt', 'r', encoding='utf8') as f:
        content = f.read()
        err_symbol = set(content.split('\n'))

    _sent = ''.join([item if item not in err_symbol else ' ' for item in sentence])
    return delete_extra_spaces(_sent)


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


# 文件操作
def list_file(folder):
    """
        get all file
    :param folder:
    :return:
    """
    file_list = []
    files = os.listdir(folder)
    for file in files:
        file_name = os.path.join(folder + "\\" + file)
        if os.path.isdir(file_name):
            file_list.extend(list_file(file_name))
        else:
            file_list.append(file_name)
    return file_list


def move_all_file(old_folder, new_folder):
    """
        move all file in old_folder to new_folder
    :param old_folder:
    :param new_folder:
    :return:
    """
    file_list = list_file(old_folder)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    for file in file_list:
        shutil.move(file, new_folder)


def move_file(file, new_folder):
    """
        move all file in old_folder to new_folder
    :param old_folder:
    :param new_folder:
    :return:
    """
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    shutil.move(file, new_folder)


def read_file(file):
    """
        读取文件
    :param file:
    :return:
    """
    with open(file, 'r', encoding='utf8') as f:
        data = f.readlines()
    return [item.strip() for item in data]


def read_rar_file(file_path, pwd=None):
    """
    读取zip压缩文件内所有文件的文件名
    :param path: 路径
    :return: []
    """
    file = rarfile.RarFile(file_path, pwd=pwd)
    return file.namelist()


# 工具性
def gen_md5(data):
    """
        生成md5
    :param data: 字符串数据
    :return:
    """
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


def remove_same(data):
    """
        去重，对于数量级小的的数据进行去重
    :param data:
    :return:
    """
    return list(set(data))


def file_remove_same(input_file, output_file):
    """
        针对小文件去重
    :param input_file: 输入文件
    :param out_file: 去重后出文件
    :return:
    """
    with open(input_file, 'r', encoding='utf8') as f, open(output_file, 'a', encoding='utf8') as ff:
        data = [item.strip() for item in f.readlines()]  # 针对最后一行没有换行符，与其他它行重复的情况
        new_data = list(set(data))
        ff.writelines([item + '\n' for item in new_data if item])  # 针对去除文件中有多行空行的情况


def big_file_remove_same(input_file, output_file):
    """
        针对大文件文件去重（将文件文件写在一行的，没有办法去重）
    :param input_file:
    :param output_file:
    :return:
    """
    finger_print_set = set()
    with open(input_file, 'r', encoding='utf8') as f, open(output_file, 'w', encoding='utf8') as ff:
        for line in f:
            line_string = line.strip()
            finger_print = gen_md5(line_string)
            if finger_print not in finger_print_set:
                finger_print_set.add(finger_print)
                ff.write(line)


if __name__ == '__main__':
    # input_file = r"C:\Users\Administrator\Desktop\aaa.txt"
    # output_file = r"C:\Users\Administrator\Desktop\bbb.txt"
    # big_file_remove_same(input_file, output_file)

    path = r"I:\学习\书"
    for file in list_file(path):
        try:
            book_names = read_rar_file(file)
        except:
            book_names = read_rar_file(file, pwd="123456")
        for book_name in book_names:
            print(book_name)
