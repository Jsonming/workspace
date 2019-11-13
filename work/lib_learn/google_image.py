#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 0:15
# @Author  : yangmingming
# @Site    : 
# @File    : google_image.py
# @Software: PyCharm

import google_images_download
import sys

sys.argv = ['googleimagesdownload', '-k', "Polar bears, baloons, Beaches", '-l', '20']
google_images_download.main()