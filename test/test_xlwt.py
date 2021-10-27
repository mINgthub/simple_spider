import xlwt
# 创建workbook对象
workbook = xlwt.Workbook(encoding='utf-8')
# 创建工作表
worksheet = workbook.add_sheet('sheet1')

col = ("xxx", "xxx", 'xxx')

# 添加数据 单元格(0, 0) 添加 'hello' (行,列)
worksheet.write(0, 0, 'hello')
# 保存
workbook.save('test.xls')
