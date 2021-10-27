# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

from urllib import request, error, parse, robotparser

# get请求测试

# data = request.urlopen("https://www.jd.com")
# # print(data.read().decode('utf-8'))
# f = open('index.html', 'wb')
# f.write(data.read())
# f.close()

# post请求测试
postData = {
    "aaa": "hello world"
}
# 封装post请求参数
# bytes() 将里面的数据变为二进制
# parse 解析url
# data = bytes(parse.urlencode({"aaa": "hello world"}), encoding="utf-8")
# response = request.urlopen("https://httpbin.org/post", data=data)
# with open('post.json', 'wb') as f:
#     f.write(response.read())
# print(response.read().decode("utf-8"))
