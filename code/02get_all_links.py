# -*- coding: utf-8 -*-
# @Time: 2021/10/30 11:29
# @File: 02get_all_links.py
# @Software: PyCharm
# 采集整个网站的信息

from urllib import request
from bs4 import BeautifulSoup
import re


allIntLinks = set()
allExtLinks = set()


# 解析bsObj获取所有的外部链接
def getExternalLinks(bsObj, externalLink):
    externalLinks = []
    # http | www 开头不包括 externalLink的字段
    for link in bsObj.findAll('a', href=re.compile("^(http|www)((?!"+externalLink+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                # print('外部链接：'+link.attrs['href'])
                externalLinks.append(link.attrs['href'])
    return externalLinks


# 解析bsObj的所有innerLink
def getInternalLinks(bsObj, internalLink):
    internalLinks = []
    # / | innerLink 开头的链接
    for link in bsObj.findAll('a', href=re.compile("^(/|.*"+internalLink+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


def splitAddress(address):
    part = address.replace("http://", "").split('/')
    return part


def getAllExternalLinks(siteUrl):
    html = None
    try:
        html = request.urlopen(siteUrl)
    except ValueError:
        print(len(allIntLinks), len(allIntLinks))
    bsObj = BeautifulSoup(html, 'html.parser')
    external_links = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    internal_links = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    print('error', len(external_links), len(internal_links))
    for link in external_links:
        if link not in allExtLinks:
            allExtLinks.add(link)
            # print(link)
    for link in internal_links:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print('即将要获取的链接是：' + link)
            getAllExternalLinks(link)


getAllExternalLinks("http://oreilly.com")