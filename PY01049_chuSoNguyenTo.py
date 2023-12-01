from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    chu_so = 0
    dem = 0
    while n > 0:
        r = n % 10
        chu_so += 1
        if r == 2 or r == 3 or r == 5 or r == 7:
            dem += 1
        n //= 10
    if nt(chu_so) == False:
        return False
    if dem > chu_so - dem:
        return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        if check(n) == True:
            print("YES")
        else:
            print("NO")
        t -= 1