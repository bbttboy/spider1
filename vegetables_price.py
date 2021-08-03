# 新发地网页已经改版，现在是客户端加载json文件

import requests
from bs4 import BeautifulSoup
import csv

url = "http"
resp = requests.get(url)

f = open("vegetables_price.csv", mode="w")
csvWriter = csv.writer(f)

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
resp.close()
# 2.从bs对象中查找数据
# find(标签, 属性=值)
# find_all(标签, 属性=值)
# table = page.find("table", class_="hq_table")  # class是python关键字
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行是一个意思，此时可以避免class
trs = table.find_all("tr")[1:]
for tr in trs:
  tds = tr.find_all("td")  # 拿到每行中的所有td
  name = tds[0].text  # .text 表示拿到被标签标记的内容
  low = tds[1].text
  avg = tds[2].text
  high = tds[3].text
  specification = tds[4].text
  place = tds[5].text
  unit = tds[6].text
  date = tds[7].text
  csvWriter.writerow([name, low, avg, high, specification, place, unit, date])

f.close()
print("over!!")