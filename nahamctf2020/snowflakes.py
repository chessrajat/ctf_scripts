import os
import time

file1 = open("/home/raat/Documents/rockyou.txt","r",encoding='latin-1')
passwds = file1.readlines()

for i in passwds:
    i = i.replace("\n", "")
    cmd = "stegsnow -C -p '{}' /home/raat/Documents/CTFs/nahamcon-ctf2020/stegnography/snowflake/frostythesnowman.txt".format(i)
    result = os.system(cmd)
    if "{" in str(result):
        print(result)
        time.sleep(0.5)




# cmd = "stegsnow -C -p 'snowman' /home/raat/Documents/CTFs/nahamcon-ctf2020/stegnography/snowflake/frostythesnowman.txt"
