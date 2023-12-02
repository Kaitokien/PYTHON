from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

def digit(n):
    ans = 0
    for i in range(len(n)):
        ans += int(n[i])
    if isPrime(ans): return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        mark = [0] * 1000001
        n = input()
        for i in range(10, int(n) + 1):
            tmp = int(str(i)[::-1])
            if isPrime(i) and isPrime(tmp) and tmp <= int(n) and str(i) != str(i)[::-1] and mark[tmp] == 0:
                print(min(i, tmp), max(i, tmp), end = ' ')
                mark[tmp] = 1
                mark[i] = 1
        print()
        t -= 1
