def gsm7bitdecode(f):
    f = ''.join(["{0:08b}".format(int(f[i:i + 2], 16)) for i in range(0, len(f), 2)][::-1])
    return ''.join([chr(int(f[::-1][i:i + 7][::-1], 2)) for i in range(0, len(f), 7)])


val = "000003340001a00020202020202000f5a00001006900006700ff9c0402030201ffff0b5a0791233010210068040b917120336603f800002140206165028047c7f79b0c52bfc52c101d5d0699d9e133283d0785e764f87b6da7956bb7f82d2c8b"
print(gsm7bitdecode(val))