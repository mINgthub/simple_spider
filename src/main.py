# 解析网页
from bs4 import BeautifulSoup
# 正则匹配
import re
# 发送请求获取网页
from urllib import request, error
# 进行excel操作
import xlwt
# 进行数据库操作
import sqlite3

baseUrl = "https://movie.douban.com/top250?start="
savePath = "豆瓣top250.xls"

# 正则匹配 (.*?) 表示0 - 无限多个字符出现0次或1次 r 表示忽略特殊字符
# 查找所有电影详情的链接
findLink = re.compile(r'<a href="(.*?)">')
# 所有的图片链接 re.S 忽略可能存在的换行符
findPicLink = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片的片名
findName = re.compile(r'<span class="title">(.*?)</span>', re.S)
# 影片评分
findRate = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 评价人数 \d 表示数字
findJudge = re.compile(r'<span>(\d*?)人评价</span>')
# 影片概况
findInq = re.compile(r'<span class="inq">(.*?)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getHtml(url):
    html = ""
    # 请求头信息 模拟真实的浏览器访问
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    # 设置请求头
    req = request.Request(url, headers=head)
    try:
        response = request.urlopen(req, timeout=10)
        html = response.read().decode("utf-8")
        # with open('douban.html', 'wb') as file:
        #     file.write(response.read())
    except error.URLError as e:
        if hasattr(e, "code"):
            print("e.code:", e.code)
        if hasattr(e, "reason"):
            print("e.reason", e.reason)
    return html


# 获取数据
def getData():
    datalist = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        html = getHtml(url)
        # 解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_="item"):
            # print(item)
            # print(str(item))
            # print(type(item)) <class 'bs4.element.Tag'>
            # 保存一部电影的全部信息
            print("正在爬取第%d条" % (len(datalist) + 1))
            data = []
            item = str(item)
            # 每一部电影详情的链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            picLink = re.findall(findPicLink, item)[0]
            data.append(picLink)
            movieName = re.findall(findName, item)
            if len(movieName) >= 2:
                # 中文名字
                cname = movieName[0]
                data.append(cname)
                # 外文名字
                ename = movieName[1].replace("\xa0/\xa0", "")
                data.append(ename)
            else:
                data.append(movieName[0])
                data.append(" ")
            rate = re.findall(findRate, item)[0]
            data.append(rate)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', '')
                data.append(inq)
            else:
                data.append(' ')
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', '', bd)
            data.append(bd.strip())
            datalist.append(data)
    # print(datalist, len(datalist[0]))
    return datalist


# 保存数据
def storeData(datalist, path):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('douban_top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "电影图片链接", "电影中文名", "电影外文名", "电影评分", "电影评价人数", "电影概况", "相关信息")
    for i in range(0, 8):
        # 填写列名
        worksheet.write(0, i, col[i])
    for i in range(0, 250):
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i+1, j, data[j])
    workbook.save(path)


def main():
    data = getData()
    storeData(data, savePath)


if __name__ == "__main__":
    main()
    print("爬取完毕")
