import requests


inp = input("输入需要翻译的内容: \n")
url = "https://fanyi.baidu.com/sug"
form_data = {"kw": inp}

resp = requests.post(url, data=form_data)
print(resp.json())