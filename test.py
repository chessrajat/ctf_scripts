import hashlib
def crack_password():
    password = "0c01f4468bd75d7a84c7eb73846e8d96"
    output = ""
    wordlist = "/home/kali/Documents/wordlists/SecLists/rockyou.txt "
    salt = "1d0t1111"
    word_dict = open(wordlist)
    for line in word_dict.readlines():
        line = line.replace("\n", "")
        print(line)
        if hashlib.md5((str(salt) + line).encode("utf-8")).hexdigest() == password:
            output += "\n[+] Password cracked: " + line
            break
    word_dict.close()
    print(output)
    
crack_password()