#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/24 0024'

"""

from extract_img import SWFExtractor
swf =SWFExtractor(package='1.swf',rdpi=200,img_path='out_img',outfile='test.png')

swf.swf2Longimg() # 普通的拼接方式

# swf.swf2longimgNowhite() # 切除空白的拼接方式

# 拼接图片

print('print SWFExtractor end ')