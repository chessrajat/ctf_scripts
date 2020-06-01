import socket
import time

host = 'chals20.cybercastors.com'
port = 14430

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print(client.recv(1024).decode())

def checkNum(val):
    if val.isdigit():
        return int(val)
    else:
        if val == "one":
            return 1
        elif val == "two":
            return 2
        elif val == "three":
            return 3
        elif val == "four":
            return 4
        elif val == "five":
            return 5
        elif val == "six":
            return 6
        elif val == "seven":
            return 7
        elif val == "eight":
            return 8
        elif val == "nine":
            return 9
        else:
            return 0


def calc(problem):
    a = ""
    for i in problem:
        a += str(int(i,2))
    return a




if __name__ == '__main__':

    f = True
    ff = False
    while True:
        res = client.recv(4096).decode()
        print(res)
        data = ""
        if not res:
            break


        if f:
            client.send("\n".encode())

        if not 'castorsCTF' in res and not f:
                problem = res.split()
                print(problem)
                ans = calc(problem)
                print(ans)
                client.send(ans.encode())
        elif f:
            f = False
        else:
            break