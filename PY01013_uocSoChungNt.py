from math import *
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def tongchuso(n):
    ans = 0
    while n > 0:
        r = n % 10
        ans += r
        n //= 10
    return ans

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        res = gcd(a, b)
        if(nt(tongchuso(res)) == True):
            print("YES")
        else:
            print("NO")
        t -= 1