from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    to = max(a)
    nho = min(a)
    tong = 0
    for i in range(0, len(a)):
        if a[i] == to  or a[i] == nho:
            n -= 1
        else:
            tong += a[i]
    print('%.2f' % (tong / n))