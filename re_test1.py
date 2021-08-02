import re

# # findall 匹配字符串中所以的符合正则的内容
# lst = re.findall(r"\d+", "电话：10086， 电话：10010")
# print(lst)

# # finditer 匹配字符串中所有的符合正则的内容[返回的是迭代器]，效率比list高
# # 从迭代器中拿到内容需要.group()
# lst = re.finditer(r"\d+", "电话：10086， 电话：10010")
# print(lst)
# for i in lst:
#   print(i)
#   print(i.group())

# # search 找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
# s = re.search(r"\d+", "电话：10086， 电话：10010")
# print(s)

# # match 从头开始匹配，即默认在pattern前面加^ (^\d+)
# s = re.match(r"\d+", "电话：10086， 电话：10010")
# print(s.group())

# # 预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("电话：10086， 电话：10010")
# for it in ret:
#   print(it.group())
# print(ret)
#
# ret = obj.findall("电话：10000")
# print(ret)

s = """
<div class='ql'><span id='1'>麒麟</span></div>
<div class='zq'><span id='2'>朱雀</span></div>
<div class='xw'><span id='3'>玄武</span></div>
<div class='bh'><span id='4'>白虎</span></div>
"""
# re.S能让.匹配换行符
# (?P<分组名字>正则)  可以单独从正则匹配内容中进一步提取内容
obj = re.compile(r"<div class='(?P<ename>.*?)'><span id='(?P<id>\d)'>(?P<name>.*?)</span></div>", re.S)
result = obj.finditer(s)
for it in result:
  print(it.group("ename"))
  print(it.group("id"))
  print(it.group("name"))