from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        tong = 0
        check = True
        for i in range(len(n)):
            tong += int(n[i])
            if i % 2 == 0:
                if int(n[i]) % 2 != 0:
                    check = False
                    break
            else:
                if int(n[i]) % 2 != 1:
                    check = False
                    break
        if check == False or nt(tong) == False:
            print("NO")
        else:
            print("YES")