from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    max_val, min_val, luck = -1, 999999999, -1
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
        max_val = max(max_val, max(a[i]))
        min_val = min(min_val, min(a[i]))
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_val - min_val:
                luck = max_val - min_val
                break
        if luck != -1: break
    if luck == -1:
        print("NOT FOUND")
    else:
        print(luck)
        for i in range(n):
            for j in range(m):
                if a[i][j] == luck:
                    print("Vi tri ", '[', i, ']', '[', j, ']', sep = '')