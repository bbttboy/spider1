import re
import requests
import csv

f = open("dytt.csv", "w", encoding='gb2312')
csvWriter = csv.writer(f)

domain = "https://dytt89.com/"

myHeader = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}

resp = requests.get(domain, verify=False, headers=myHeader)  # verify=False 去掉安全验证
resp.encoding = "gb2312"
content = resp.text
resp.close()

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<li><a href='(?P<href>.*?)'.*?</li>", re.S)
obj3 = re.compile(r'<title>.*?《(?P<name>.*?)》.*?</title>.*?><a href="magnet:.*?">(?P<magnet>.*?)</a></td>', re.S)

result1 = obj1.finditer(content)
result2 = obj2.finditer(result1.__next__().group("ul"))

child_url = []
for href in result2:
  child_url.append(href.group("href"))

for href in child_url:
  url = domain + href.strip('/')
  resp_child = requests.get(url, verify=False, headers=myHeader)
  resp_child.encoding = "gb2312"
  content_child = resp_child.text
  resp_child.close()
  result3 = obj3.search(content_child)
  dic = result3.groupdict()
  csvWriter.writerow(dic.values())

f.close()


