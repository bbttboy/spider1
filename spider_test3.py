import requests

url = ""
params = {

}

resp = requests.get(url, params=params)
print(resp.json())
