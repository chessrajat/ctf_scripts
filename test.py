# from tqdm import tqdm

# val = 11111111111111

# for val in tqdm(range(val,99999999999999)):

#     v1 = 0
#     v2 = 0
#     while True:
#         input_len = len(str(val))
#         if input_len <=v2:
#             break
#         v1 = v1 + int(str(val)[v2])
#         v2 = v2 + 1
#     if v1 == 1000:
#         print("Found value")
#         print(v1)
#         break

# print("not found")

val = "n"
v1 = 0
v2 = 0
while True:
    v1 = v1 + int(ord(val[v2]))
    v2 = v2 + 1
    print(val)
    

    if v1 > 850 and v1 < 900:
        print(v1)
        print(val)
        val += "x"

    if v1 == 1000:
        print("yes found it")
        print(val)
        break
    val += "n"
