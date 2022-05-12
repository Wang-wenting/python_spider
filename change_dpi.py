#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 11:28
# @Author  : RooFTOooOP
# @FileName: change_dpi.py
# @Software: PyCharm

from PIL import Image as ImagePIL
import os


def transfer(infile, outfile):
    im = ImagePIL.open(infile)
    im.save(outfile, dpi=(96.0, 96.0))  ##500.0,500.0分别为想要设定的dpi值

# path = 'E:\英雄推荐系统\data\image\\top'
# file = os.listdir(path)
# for f in file:
#     print(f)
#     name = path + '\\' + f
#     transfer(name, name)

os.system('backgroundremover -i "E:\英雄推荐系统\\background\\lol.jpg" -o "E:\英雄推荐系统\\background\\lol1.jpg"')