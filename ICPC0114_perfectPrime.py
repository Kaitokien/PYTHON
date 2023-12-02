from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

def digit(n):
    ans = 0
    for i in range(len(n)):
        if n[i] != '2' and n[i] != '3' and n[i] != '5' and n[i] != '7':
            return False
        ans += int(n[i])
    if isPrime(ans): return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        if isPrime(int(n)) and isPrime(int(n[::-1])) and digit(n):
            print("Yes")
        else: print("No")
        t -= 1
