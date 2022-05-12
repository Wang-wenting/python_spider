#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 10:36
# @Author  : RooFTOooOP
# @FileName: startproxy.py
# @Software: PyCharm


# -*- coding:UTF-8 -*-
from mitmproxy.tools._main import mitmweb
mitmweb(args=['-s', './HttpProxy.py', '-p', '9000', '--web-port', '9020'])