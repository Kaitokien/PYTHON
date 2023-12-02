from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, dem = int(input()), 0
        for i in range(2, n + 1):
            if isPrime(i):
                if i + 2 <= n and isPrime(i + 2):
                    if i + 6 <= n and isPrime(i + 6):
                        dem += 1
                if i + 4 <= n and isPrime(i + 4):
                    if i + 6 <= n and isPrime(i + 6):
                        dem += 1
        print(dem)
        t -= 1