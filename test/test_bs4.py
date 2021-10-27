# coding = "utf-8"
# beautifulSoup中文文档： https://beautifulsoup.cn/
from bs4 import BeautifulSoup
import re

with open('./prettify.html', 'rb') as file:
    html = file.read()
    # 指定解析器 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')
    # print(type(soup))
    # print(type(soup.a))
    # print(type(soup.a.string))
    # print(type(soup.a.attrs))
    # print(type(soup.div['id']))
    # print(type(soup.get_text()))
    # print(type(soup.prettify()))
    """
        <class 'bs4.BeautifulSoup'>
        <class 'bs4.element.Tag'>
        <class 'bs4.element.NavigableString'>
        <class 'dict'>
        <class 'str'>
        <class 'str'>
        <class 'str'>
    """
    # print(soup.a)
    # print(soup.a['class'])
    # print(soup.a.string)
    # print(soup.a.attrs)
    # print(soup.a.attrs['href'])
    # print(soup.prettify())
    # print(soup.find_all('a'))
    # print(soup.div['id'])
    # print(soup.find(id="db-global-nav"))
    # print(soup.get_text())
    # ----------------------------------------- #
    # 文档的遍历
    # 列表通过下表访问
    # print(type(soup.head))
    # print(soup.head.contents)
    # print(type(soup.head.contents))
    # ----------------------------------------- #
    # 文档的搜索
    """
        字符串搜索
        1. find_all() # 返回一个列表
        2. find()   # 返回找到的元素
        正则使用search()搜索
        find_all(re.compile("a"))
        使用函数搜索
        def is_exist_attr():
            return tag.has_attr("name")
        find_all(is_exist_attr)
        kwargs 参数搜索
        find_all(id="aaa")
        find_all(class=True)
        find_all(href="xxx.com")
        find_all(class_="aaa")
        find_all(text="登录") 或者
        find_all(text=["登录", 'hao123', '地图'])
        limit 参数
        find_all('a', limit = 2)
        css选择器搜索
        select()
    """
    # print(soup.find_all('a'))
    # print(soup.find_all('a')[0])
    # print(type(soup.find_all('a')))
    # print(soup.find_all('a', limit=3))
    # print(soup.find_all(id=True, limit=2))
    print(soup.select('#db-global-nav'))
# Tag soup.tag 拿到第一个标签
