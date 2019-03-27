#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/24 0024'

"""

import os
from subprocess import Popen, PIPE, call
from PIL import Image


class SWFExtractor(object):
    '''

    '''

    def __init__(self, package, outfile, rdpi=None, img_path=None):
        self.tool_name = 'swf2img.exe'
        self.package = package
        self.r = rdpi
        self.o = outfile
        self.path = img_path
        self.is_available = self.check_command(self.tool_name)
        self.create_directory_if_not_exists(img_path)
        self.Basedir = os.path.abspath(os.path.dirname(__file__))

    def check_command(self, command):
        result = True
        try:
            p = Popen([command], stdout=PIPE, stderr=PIPE)
            out, err = p.communicate()
        except:
            result = False
        finally:
            pass
        return result

    def create_directory_if_not_exists(self, dir_name):  # 创建目录
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def extract_img(self):
        if not self.is_available:
            return False

        if not os.path.exists(self.package):
            print('SWF file not found: ' + self.package)
            return False

        if self.r == None:
            self.r = 150
        outpath = os.path.join(self.path, self.o)
        command = [self.tool_name, self.package, '-r', str(self.r), '-o', outpath]
        p = Popen(command, stderr=PIPE, stdout=PIPE)
        out, err = p.communicate()
        if err:
            print('extractor error:', err)
            return err

        return True

    def swf2img(self):
        if not self.extract_img():
            print('Failed to extract images')
            return False

    def swf2Longimg(self):  # 转换长图片。
        if not self.extract_img():
            print('Failed to extract images')
            return False
        else:
            try:
                out_img_path = os.path.join(self.Basedir, self.path)
                imgs = [Image.open(os.path.join(out_img_path, p)) for p in os.listdir(out_img_path)]
                width, height = imgs[0].size
                long_img = Image.new('RGB', (width, height * len(imgs)), 'white')
                for i, im in enumerate(imgs):
                    long_img.paste(im, box=(0, i * height))
                long_img.save(os.path.join(out_img_path, 'long_{}'.format(self.o)))
                return True
            except Exception as e:
                print(e)
                return False

    def swf2longimgNowhite(self, white_h=210):
        if not self.extract_img():
            print('Failed to extract images')
            return False
        else:
            try:
                out_img_path = os.path.join(self.Basedir, self.path)
                imgs = [Image.open(os.path.join(out_img_path, p)) for p in os.listdir(out_img_path)]
                width, height = imgs[0].size
                long_img = Image.new('RGB', (width, (height - 2 * white_h) * len(imgs) + white_h), 'white')
                i = 0
                for img in imgs:
                    newimg = img.crop((0, white_h, width, height - white_h))
                    long_img.paste(newimg, box=(0, white_h + i * (height - 2 * white_h)))
                    i += 1
                long_img.save(os.path.join(out_img_path, 'long_{}'.format(self.o))) # 可以更换存储的方式
                return True
            except Exception as e:
                print(e)
                return False
