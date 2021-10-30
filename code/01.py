# -*- coding: utf-8 -*-
# @Time: 2021/10/29 9:53
# @File: 01.py
# @Software: PyCharm
# 获取整个网站的内链和外链

from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import re
import datetime
import random
pages = set()
random.seed(datetime.datetime.now())


# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    # 匹配http或者www开头的且不包含当前url的单个字符无限次扩展
    # href=re.compile("^(http|www)((?!oreilly.com).)*$")
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


# http://oreilly.com ==> ['oreilly.com']
def splitAddress(address):
    addressParts = address.replace("https://", "").split("/")
    return addressParts


num = 0


def getRandomExternalLink(startingPage):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    req = request.Request(startingPage, headers=head)
    html = urlopen(req)
    bsObj = BeautifulSoup(html, 'html.parser')
    global num
    num = num + 1
    print(num)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    # print(externalLinks)
    if len(externalLinks) == 0:
        # 如果不存在外链就随机进入一个内链
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("https://baidu.com/")
    print("随机外链是： "+externalLink)
    followExternalOnly(externalLink)


followExternalOnly("https://www.baidu.com/")

