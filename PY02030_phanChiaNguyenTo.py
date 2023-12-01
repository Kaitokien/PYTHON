from math import *

def nt(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b, se, pre, idx = [], set(), [], -1
    for i in range(len(a)):
        if a[i] not in se:
            b.append(a[i])
            se.add(a[i])
    pre.append(b[0])
    for i in range(1, len(b)):
        pre.append(b[i] + pre[i - 1])
    for i in range(len(b) - 1):
        if nt(pre[i]) and nt(pre[len(b) - 1] - pre[i]):
            idx = 0
            print(i)
            break
    if idx == -1: print("NOT FOUND")