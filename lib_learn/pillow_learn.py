#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 17:03
# @Author  : yangmingming
# @Site    : 
# @File    : pillow_learn.py
# @Software: PyCharm
import matplotlib.pyplot as plt
from PIL import Image

img_path = r"C:\Users\Administrator\Desktop\test\canliechehuo151.jpg"

# img = Image.open(img_path)
# img.show()

img = Image.open(img_path)
# plt.figure("dog")
plt.imshow(img)
plt.show()
