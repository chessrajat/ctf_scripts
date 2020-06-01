import socket
import time

host = 'chals20.cybercastors.com'
port = 14429

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

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
    a = checkNum(problem[2])
    b = checkNum(problem[4])
    op = problem[3]
    if op == '+' or op=="plus":
        return str(a + b)
    elif op == '-' or op == "minus":
        return str(a - b)
    elif op == '*' or op == "multiplied-by":
        return str(a * b)
    elif op == '//' or op == "divided-by":
        return str(a // b)


if __name__ == '__main__':

    f = True
    ff = False
    while True:
        res = client.recv(1024).decode()
        print(res)
        if not res:
            break


        if f:
            client.send("\n".encode())

        if not 'castorsCTF' in res and not f:
            if "?" in res:
                time.sleep(0.2)
                problem = res.split()
                if len(problem)>6:
                    problem = problem[2:]
                print(problem)
                ans = calc(problem)
                print(ans)
                client.send(ans.encode())
            else:
                continue
        elif f:
            f = False
        else:
            break