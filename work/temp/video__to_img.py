#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:54
# @Author  : yangmingming
# @Site    : 
# @File    : video__to_img.py
# @Software: PyCharm
import cv2
import os


def video_to_img(video_file=None, to_path=None):
    """
    将视频转换为图片
    :param video_file:视频文件
    :param to_path: 图片存储地址
    :return:
    """

    cap = cv2.VideoCapture(video_file)
    for i in range(1, 10):
        print(cap.get(i))

    count, success = 1, True
    while success:
        success, frame = cap.read()
        org_name = video_file.split('\\')[-1].split('.')[1]
        img_name = os.path.join(to_path, "{}_{}.jpg".format(org_name, count))
        print(img_name)
        cv2.imwrite(img_name, frame)
        count += 1
    cap.release()


if __name__ == '__main__':
    video_file = r"C:\Users\Administrator\Desktop\work\src\indoor_frontal_left.mp4"
    path = r"C:\Users\Administrator\Desktop\work\res\new"
    video_to_img(video_file=video_file, to_path=path)
