#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 22:47
# @Author  : yangmingming
# @Site    : 
# @File    : ffmpeg.py
# @Software: PyCharm

import os
import subprocess

current = os.getcwd()
dirs = os.listdir(current)
for i in dirs:
    if os.path.splitext(i)[1] == ".mp4":
        bname = str(os.path.splitext(i)[0].encode('utf-8')).replace('\\','%').replace(' ','_')
        os.rename(i, 'temp.mp4')
        getmp3 = 'ffmpeg -i temp.mp4 -f mp3 -vn temp.mp3'
        cutmp3 = 'ffmpeg -i temp.mp3 -ss 00:00:15 -acodec copy tempcut.mp3'
        returnget = subprocess.call(getmp3, shell=True)
        returncut = subprocess.call(cutmp3, shell=True)
        os.remove('temp.mp3')
        os.rename('tempcut.mp3', os.path.splitext(i)[0] + '.mp3')
        os.rename('temp.mp4', i)
        print(returnget, returncut)
