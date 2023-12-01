from math import *

def nt(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

n, b = int(input()), []
a = list(map(int, input().split()))
for item in a:
    if nt(item):
        b.append(item)
b.sort()
idx = 0
for i in range(len(a)):
    if nt(a[i]) == False:
        print(a[i], end = ' ')
    else:
        print(b[idx], end = ' ')
        idx += 1