import requests
from bs4 import BeautifulSoup

url = "https://www.umei.cc/bizhitupian/meinvbizhi/dongmammeinv.htm"
main_url = "https://www.umei.cc"

headers = {
  "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}

main_resp = requests.get(url, headers=headers)
main_resp.encoding = "utf-8"

# 把页面源代码交给bs解析
bs_main = BeautifulSoup(main_resp.text, "html.parser")
main_resp.close()

a_list = bs_main.find("div", attrs={"class": "TypeList"}).find_all("a")

for a in a_list:
  # 拿到子页面源代码
  href = a.get("href")  # 直接通过get就可以拿到属性的值
  child_resp = requests.get(main_url+href, headers=headers)
  child_resp.encoding = "utf-8"
  # 从子页面拿到下载地址
  bs_child = BeautifulSoup(child_resp.text, "html.parser")
  child_resp.close()
  img_src = bs_child.find("div", attrs={"class": "ImageBody"}).find("img").get("src")
  # 下载图片
  img_resp = requests.get(img_src)
  # img_resp.content  # 这里拿到的是字节
  img_name = img_src.split("/")[-1]
  with open("umei_imgs/"+img_name, "wb") as f:
    f.write(img_resp.content)  # 图片内容写入文件
    f.close()
  print("over!  ", img_name)

print("all over!!")
