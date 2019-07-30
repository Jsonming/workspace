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
from PIL import Image
import cv2 as cv
import pandas as pd


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


def imgage_filter(img_path, to_folder):
    """ 图片打开时间设置为10秒, 移动至temp文件下按“0”键，按其他键查看下一张图片"""
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
        temp_folder = to_folder
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        shutil.move(img_path, temp_folder)


def pixel_count(folder):
    """
        像素统计
    :param img_path: 图片路径
    :return:
    """
    files = list_file(folder)
    h, w = [], []
    for file in files:
        try:
            imgage = cv.imread(file)
            height, width, *_ = imgage.shape
        except:
            print(file)
        else:
            h.append(height)
            w.append(width)
    df = pd.DataFrame({'height': h, 'width': w})
    pixel = df.apply(lambda x: x[0] * x[1], axis=1).sort_values()
    print(pixel.describe())


def run():
    folder = r"C:\Users\Administrator\Desktop\image\image\abnormal\car_chehuo"
    # to_folder = r"C:\Users\Administrator\Desktop\temp"
    # folder = r"C:\Users\Administrator\Desktop\temp"
    pixel_count(folder)


if __name__ == '__main__':
    run()
