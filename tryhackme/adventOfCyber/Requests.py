import requests
import json

url = "http://10.10.169.100:3000"
port = 3000

res = requests.get(url)
data = json.loads(res.text)

value = []
value.append(data["value"])
next = data["next"]

while(next != "end"):
    new_url = "{}/{}".format(url,next)
    print(new_url)
    res = requests.get(new_url)
    data = json.loads(res.text)
    value.append(data["value"])
    next = data["next"]

print("".join(value))