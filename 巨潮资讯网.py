#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 11:31
# @Author  : RooFTOooOP
# @FileName: get_pdf.py
# @Software: PyCharm



import requests
import random
import time



download_path= 'http://static.cninfo.com.cn/'
saving_path= 'E://对外投资//食品对外投资'

User_Agent= [
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"
    ]                                #User_Agent的集合

headers= {'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
          'Host': 'www.cninfo.com.cn',
           'Origin': 'http://www.cninfo.com.cn',
           'Referer': 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice',
            'X-Requested-With': 'XMLHttpRequest'
          }

def single_page(page):
    # target = 'http://www.cninfo.com.cn/new/fulltextSearch/full?searchkey=%E9%A3%9F+%E5%AF%B9%E5%A4%96%E6%8A%95%E8%B5%84&sdate=&edate=&isfulltext=false&sortName=pubdate&sortType=desc&pageNum=' + str(page+1)
    # target = 'http://www.cninfo.com.cn/new/index'
    target = 'http://www.cninfo.com.cn/new/fulltextSearch'
    # target = 'http://www.cninfo.com.cn/new/disclosure'
    # payload = {'column': 'szse_latest',
    #             'pageNum': 3,
    #             'pageSize': 30,
    #             'sortName': '',
    #             'sortType': '',
    #             'clusterFlag': 'true',}
    payload = {'searchkey':'%E9%A3%9F+%E5%AF%B9%E5%A4%96%E6%8A%95%E8%B5%84',
               'sdate':'',
               'edate':'',
               'isfulltext':'false',
               'sortName':'pubdate',
               'sortType':'desc',
               'pageNum':page+1}
    # pay = str(payload)
    headers['User-Agent'] = random.choice(User_Agent)
    req = requests.post(url=target, headers=headers, data=payload)
    return req.json()['classifiedAnnouncements']


def saving(single_page):          #下载年报
    headers= {'Accept': 'application/json, text/javascript, */*; q=0.01',
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
               }
    for i in single_page:
        download = download_path + i["adjunctUrl"]
        name = i['announcementTitle'] + '.pdf'

        name = name.replace('[', '')
        name = name.replace(']', '')
        name = name.replace(':', '：')
        name = name.replace('<em>', '')
        name = name.replace('</em>', '')
        file_path = saving_path + '//' + name
        time.sleep(random.random() * 4)
        headers['User-Agent'] = random.choice(User_Agent)
        r = requests.get(download, headers=headers)
        if r.status_code == 200:
            f = open(file_path, "wb")
            f.write(r.content)
            f.close()
            print(name)


for k in range(32):
    page_data = single_page(k)
    saving(page_data)