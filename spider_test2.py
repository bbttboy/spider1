import requests

inp = input("输入要查询的内容: \n")
url = f"https://www.sogou.com/web?query={inp}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

resp = requests.get(url, headers=header)
print(resp.text)