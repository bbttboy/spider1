import requests

url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

myHeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

resp = requests.get(url=url, params=params, headers=myHeader)
print(resp.request.url)
print(resp.json())
resp.close()  # 关掉request，避免访问次数过多
