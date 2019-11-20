#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 17:37
# @Author  : yangmingming
# @Site    : 
# @File    : img_compress.py
# @Software: PyCharm
from PIL import Image
import os


# 图片压缩批处理
def compressImage(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)

        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        if os.path.isfile(srcFile):
            sImg = Image.open(srcFile)
            w, h = sImg.size

            ratio = min(w/480, h/768) - 0.1
            dImg = sImg.resize((int(w / ratio), int(h / ratio)), Image.ANTIALIAS)  # 设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(dstFile)  # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的

        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


if __name__ == '__main__':
    import time

    try:
        compressImage("img", 'new')
    except Exception as e:
        print("在文件的同级目录创建图片文件夹img，压缩后文件在同级目录new文件夹")
        time.sleep(5)
