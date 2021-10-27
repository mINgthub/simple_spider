import re

par = re.compile("AA")

m = par.search("ABAAACAAA")
# re.search('规则', 字符串)

print(m)
