import requests
from tqdm import tqdm


with open("./BasicTools/wordlist.txt", "r") as f:
    words = f.readlines()

IP = "10.10.97.95"

for word in tqdm(words, position=-1):
    url = f"http://{IP}/{word.strip()}.html"
    res = requests.get(url, verify=False)
    if res.status_code != 404:
        print(f"{url} --> {res.status_code}")
    # print(url)