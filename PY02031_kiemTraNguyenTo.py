from math import *
mark = [1] * 1005
def sieve():
    mark[0] = 0
    mark[1] = 0
    for i in range(2, 32):
        if mark[i] == 1:
            for j in range(i * i, 1005, i):
                mark[j] = 0
            
if __name__ == '__main__':
    sieve()
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            a[i][j] = mark[a[i][j]]
    for i in range(n):
        for j in range(m):
            print(a[i][j], end = ' ')
        print()