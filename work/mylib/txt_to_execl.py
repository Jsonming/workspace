#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 14:30
# @Author  : yangmingming
# @Site    : 
# @File    : txt_to_execl.py
# @Software: PyCharm
import os
import pandas as pd
import numpy as np
from work.mylib import list_file


def text_to_execl(file, to_folder):
    """ text 转execl"""
    if not os.path.exists(to_folder):
        os.mkdir(to_folder)

    with open(file, 'r', encoding='utf8')as f:
        data = f.readlines()

    data_split_group = [data[i: i + 10000] for i in range(0, len(data), 10000)]
    for index, data_unit in enumerate(data_split_group):
        data_unit = [item.strip() for item in data_unit]
        df = pd.DataFrame(data_unit)
        df.to_excel('{}/{}.xls'.format(to_folder, str(index)), header=False, index=False)


def folder_text_to_execl(old_folder, new_folder):
    """
        Convert the text file in the old folder to the same name xls file in the new folder
    :param old_folder:
    :param new_folder:
    :return:
    """
    file_list = list_file(old_folder)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    for file in file_list:
        print(file)
        with open(file, 'r', encoding='utf8')as f:
            data = f.read()
        data = data.split('\n')
        new_file = new_folder + "\\" + os.path.basename(file)
        new_file = new_file.replace('txt', 'xls')
        pf = pd.DataFrame(data)
        pf.to_excel(new_file, header=False, index=False)


def read_execl(file):
    """ 读execl"""
    try:
        data = pd.read_excel(file, sheet_name="content")
    except:
        try:
            data = pd.read_excel(file, sheet_name="Sheet1")
        except:
            data = pd.read_excel(file, sheet_name="news_content")

    data = np.array(data).tolist()
    data = [item[0] for item in data]
    return data


def save_txt(result, file):
    """ 保存 text"""
    with open(file, 'a', encoding='utf8')as f:
        f.write('\n'.join(result))


def execl_to_text(folder, file):
    """execl 转text"""
    data = []
    for file_a in os.listdir(folder):
        file_name = folder + r"\{}".format(file_a)
        data_ = read_execl(file_name)
        data.extend(data_)
    data = list(set(data))
    save_txt(data, file)


if __name__ == '__main__':
    # folder_one = r"C:\Users\Administrator\Desktop\indonesia_news_content.txt"
    # folder_two = r"C:\Users\Administrator\Desktop\indonesia_news_second"
    # text_to_execl(folder_one, folder_two)

    folder = r"C:\Users\Administrator\Desktop\malaysia_third\goods_name"
    file = r"C:\Users\Administrator\Desktop\malaysia_third\goods_name.txt"
    execl_to_text(folder, file)
