from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    mark = [0] * 1000005
    for i in range(len(a)):
        if nt(a[i]) == True:
            mark[a[i]] += 1
    for i in range(len(a)):
        if mark[a[i]] != 0:
            print(a[i], mark[a[i]])
            mark[a[i]] = 0