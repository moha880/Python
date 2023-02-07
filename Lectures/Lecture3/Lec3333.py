import requests

url =requests.get("https://api.ipify.org/?format=json")
ip=url.json()["ip"]

url = ""+ip+""

url = requests.get(url)
print(url.json())

