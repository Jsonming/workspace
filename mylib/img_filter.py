#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 17:21
# @Author  : yangmingming
# @Site    : 
# @File    : img_filter.py
# @Software: PyCharm
import os
import shutil
import time
import matplotlib.pyplot as plt
# from PIL import Image
import cv2 as cv


# from .move_file import list_file


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


def imgage_filter(img_path):
    # img = Image.open(img_path)
    # plt.imshow(img)
    # plt.show()
    """ 图片打开时间设置为10秒"""
    try:
        src = cv.imread(img_path)
        cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
        cv.imshow('input_image', src)
        key = cv.waitKey(10000)
        cv.destroyAllWindows()
    except:
        key = 0
        print(img_path)
    if key == 48:
        print(img_path)
        temp = img_path.split('\\')
        temp[-2] = "temp"
        temp_folder = '\\'.join(temp[:-1])
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        shutil.move(img_path, temp_folder)


def run():
    folder = r"C:\Users\Administrator\Desktop\test"
    files = list_file(folder)
    print("移动至temp文件下按“0”键，按其他键查看下一张图片")
    for file in files:
        imgage_filter(file)


if __name__ == '__main__':
    run()
