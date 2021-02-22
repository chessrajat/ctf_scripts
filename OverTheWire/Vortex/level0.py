import socket
import struct

#using struct to unpack the raw data
host = "vortex.labs.overthewire.org"
port = 5842

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

final = 0
for i in range(0,4):
    data = client.recv(4) #reading 4 byte at a time
    final += struct.unpack("<I",data)[0] # <I is the format character for unsigned integer

client.send(struct.pack("<I",final))
response = client.recv(1024).decode()
client.close()
print(response)



