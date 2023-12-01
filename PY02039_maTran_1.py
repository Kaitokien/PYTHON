from math import *

if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    k = int(input())
    tren = 0 
    duoi = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                tren += a[i][j]
            elif i > j:
                duoi += a[i][j]
    if abs(tren - duoi) <= k:
        print("YES")
    else: print("NO")
    print(abs(tren - duoi))