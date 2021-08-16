# 拿到页面源代码
# 提取和解析数据

import requests
from lxml import etree

url = "https://wenshan.zbj.com/search/f/?kw=Saas"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/92.0.4515.131 Safari/537.36"
}

resp = requests.get(url, headers=user_agent)
resp.encoding = "utf-8"
resp.close()
# 解析
html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")
for div in divs:
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")
    if price:  # 广告判断
        price = price[-1].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    company = div.xpath("./div/div/a[2]/div[1]/p/text()")
    if company:
        company = company[-1].strip()
    if price:
        print(price, title, company)


