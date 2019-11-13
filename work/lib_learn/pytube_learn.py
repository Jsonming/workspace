#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 23:51
# @Author  : yangmingming
# @Site    : 
# @File    : pytube.py
# @Software: PyCharm

from pytube import YouTube
import google_images_download

YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()