import requests
import re
import csv

url = "https://movie.douban.com/top250"

myHeader = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}

resp = requests.get(url=url, headers=myHeader)
content = resp.text
# 关闭链接
resp.close()

# 预编译正则
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<count>.*?)人评价</span>'
                 r'.*?</li>', re.S)
# 匹配内容，返回迭代器
result = obj.finditer(content)

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

for it in result:
  dic = it.groupdict()
  dic["year"] = it.group("year").strip()
  csvwriter.writerow(dic.values())

# 关闭文件
f.close()