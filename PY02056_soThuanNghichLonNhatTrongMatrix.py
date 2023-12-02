from math import *

def check(n):
    n = str(n)
    if n == n[::-1]: return True
    else: return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    max_tn = -1
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if check(a[i][j]) and a[i][j] > 10:
                max_tn = max(max_tn, a[i][j])
    if max_tn == -1:
        print("NOT FOUND")
    else:
        print(max_tn)
        for i in range(n):
            for j in range(m):
                if a[i][j] == max_tn:
                    print("Vi tri ", '[', i, ']', '[', j, ']', sep = '')