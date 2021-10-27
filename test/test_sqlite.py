import sqlite3

conn = sqlite3.connect('test.db')
print('创建成功。。')

# 获取游标
c = conn.cursor()
# sql语句
sql = '''
    
'''

c.execute(sql)
# 提交
conn.commit()
# 关闭数据库
conn.close()
