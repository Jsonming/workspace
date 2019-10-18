#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 17:23
# @Author  : yangmingming
# @Site    : 
# @File    : img_to_video.py
# @Software: PyCharm

import os
import cv2


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


path = r'C:\Users\Administrator\Desktop\00013_market\frames'
filelist = list_file(path)

fps = 1  # 视频每秒帧数
size = (1920, 1080)  # 图片分辨率
video = cv2.VideoWriter("VideoTest1.avi", cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps, size)  # 视频保存在当前目录下

for item in filelist:
    p = os.path.join(path, item)
    img = cv2.imread(p)
    video.write(img)

video.release()
cv2.destroyAllWindows()
