#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 17:44
# @Author  : yangmingming
# @Site    : 
# @File    : move_file.py
# @Software: PyCharm
import os
import shutil


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


def move_file(old_folder, new_folder):
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


# if __name__ == '__main__':
#     old_folder = r"C:\Users\Administrator\Desktop\替换词"
#     new_folder = r"C:\Users\Administrator\Desktop\malaysia_first"
#     move_file(old_folder, new_folder)


