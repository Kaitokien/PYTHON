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
    tu_dien = {}
    b = []
    for i in range(len(a)):
        if str(a[i]) not in tu_dien:
            b.append(a[i])
            tu_dien[str(a[i])] = 1
    prefix_sum = []
    for i in range(len(b)):
        if i == 0:
            prefix_sum.append(b[i])
        else:
            prefix_sum.append(prefix_sum[i - 1] + b[i])
    check = False
    for i in range(len(prefix_sum)):
        if nt(prefix_sum[i]) and nt(prefix_sum[len(prefix_sum) - 1] - prefix_sum[i]):
            check = True
            print(i)
            break
    if check == False:
        print("NOT FOUND")