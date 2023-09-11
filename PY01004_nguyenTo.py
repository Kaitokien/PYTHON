from math import *
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    if a == 1:
        return True
    return False

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
        n = int(input())
        dem = 0
        for i in range(1, n):
            if gcd(i, n) == True:
                dem += 1
        if nt(dem) == True:
            print("YES")
        else:
            print("NO")
        t -= 1