# -*- coding: utf-8 -*-
# @Time: 2021/10/29 14:19
# @File: 01study.py
# @Software: PyCharm
from urllib import request, error
from bs4 import BeautifulSoup
import re
import random
import datetime

# 初始化随机序列

random.seed(datetime.datetime.now())


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}


# 保存页面全部的链接
pages = set()


# 解析bsObj的所有innerLink
def getAllInternalLinks(bsObj, internalLink):
    internalLinks = []
    # / | innerLink 开头的链接
    for link in bsObj.findAll('a', href=re.compile("^(/|.*"+internalLink+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                # print('内部链接：'+link.attrs['href'])
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 解析bsObj获取所有的外部链接
def getAllExternalLinks(bsObj, externalLink):
    externalLinks = []
    # http | www 开头不包括 externalLink的字段
    for link in bsObj.findAll('a', href=re.compile("^(http|www)((?!"+externalLink+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                # print('外部链接：'+link.attrs['href'])
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    part = address.replace("http://", "").split('/')
    return part


def getBsObj(startPage):
    # print(startPage)
    req = request.Request(startPage, headers=headers)
    html = None
    try:
        html = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print('code', e.code)
        if hasattr(e, 'reason'):
            print('reason', e.reason)
    if html is not None:
        bsObj = BeautifulSoup(html, 'html.parser')
        return bsObj


baseUrl = 'http://jd.com'
addressPart = splitAddress(baseUrl)[0]
i = 0


def getRandomExternalLink(startPage):
    bsObj = getBsObj(startPage)
    externalLinks = getAllExternalLinks(bsObj, addressPart)
    internalLinks = getAllInternalLinks(bsObj, addressPart)
    global i
    if len(externalLinks) == 0:
        # 不存在外链
        """
            进入随机进入一个内链，随机获取一个外链
        """
        internalLink = internalLinks[i]
        i += 1
        print("不存在外链"+str(i))
        getRandomExternalLink(internalLink)
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


m = 0


def main():
    global m
    m += 1
    randomExternalLink = getRandomExternalLink(baseUrl)
    print('第%d随机外链：%str' % (m,randomExternalLink))
    main()


if __name__ == '__main__':
    main()
    # print(baseUrl, addressPart)
