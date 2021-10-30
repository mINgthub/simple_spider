# -*- coding: utf-8 -*-
# @Time: 2021/10/28 16:53
# @File: test_random_seed.py
# @Software: PyCharm

import random
# 随机数初始化
random.seed(45)  # 以 45 生成一个随机序列
print('----------------')
print(random.random())  # 初始化序列第一个值
print(random.random())  # 初始化序列第二个值
print(random.random())
print(random.random())

random.seed(45)
print('----------------')
print(random.random())  # 初始化序列第一个值
print(random.random())  # 初始化序列第二个值
print(random.random())
print(random.random())

# 两次打印的结果完全相同
