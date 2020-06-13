
import pwn
file1 = open("/home/raat/Documents/rockyou.txt","r",encoding='latin-1')
passwds = file1.readlines()

file2 = open("/home/raat/Documents/CTFs/nahamcon-ctf2020/crypto/docxor/homework","rb")
p = file2.readlines()

pwn.xor("KEY", "RAW_BINARY_CIPHER")



