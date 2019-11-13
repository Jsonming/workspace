#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 9:56
# @Author  : yangmingming
# @Site    : 
# @File    : pydub_learn.py
# @Software: PyCharm

from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import make_chunks

length = 5

sound1 = AudioSegment.from_wav(r"E:\学习用临时目录\dome.wav")
sound2 = AudioSegment.from_mp3(r"E:\学习用临时目录\demo.mp3")

louder = sound1 + 6  # sound1
quieter = sound1 - 6  # sound1
combined = sound1 + sound2  # sound1
duration_in_milliseconds = len(sound1)  # 获取sound的时长
beginning = sound1[:5000]  # 获取sound1的前5秒音频数据
end = sound1[-5000:]  # 获取sound1的后5秒音频数据

"""
    1.对于多个音频的计算，需要多个音频之间的通道数、帧数、采样率以及比特数都一样，否则低质量的音频会向高质量的转换，单声道会向立体声转换，低帧数向高帧数转换。
    2. AudioSegment原生就支持wav和raw，如果其他文件需要安装ffmpeg。raw还需要，sample_width，frame_rate，channels三个参数。
"""

with_style = beginning * 3
awesome = with_style.fade_in(2000).fade_out(3000)
beginning_file_handle = with_style.export(r'C:\Users\Administrator\Desktop\export.mp3', format='mp3')
