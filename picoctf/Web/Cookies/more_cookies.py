import requests

url = "http://mercury.picoctf.net:34962/"

cookies = {"auth_name":"S21XNG1VZytGdy9rQ3lkRUc4NnI0eEdLMm1pRGFrN01tKzRLalFiZzZQcGhLWWZ5djNrdlV1RlFDeFlrcnB2eGVtekJvbFhqMkwwNjRYT2ZtRWpWUjFrSFViNWNCTkJXVkdoVjVvUDdXZWxGLzF0czlEMDNXUTZlZnd2T2pKRlk="}

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

res = requests.get(url,headers=headers, cookies=cookies, allow_redirects=True)

print(res.url)
print(res.headers)