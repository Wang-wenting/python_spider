#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 17:11
# @Author  : RooFTOooOP
# @FileName: 1_3动漫.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41800366

from bs4 import BeautifulSoup
import requests, sys


url = 'https://www.dmzj.com/view/yaoshenji/41917.html#@page=2'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
           'Accept-Language': 'zh-CN'}
req = requests.get(url=url, headers=headers)
html = req.text
div_bf = BeautifulSoup(html)
div = div_bf.find_all('div', class_='comic_wraCon autoHeight')
print(str(div))