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
        ans = 0
        n = input()
        for i in range(len(n)):
            ans += int(n[i])
        if nt(ans) == True:
            print("YES")
        else:
            print("NO")
        t -= 1