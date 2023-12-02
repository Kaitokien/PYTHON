from math import *

def nt(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    max_prime = -1
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]):
                max_prime = max(max_prime, a[i][j])
    if max_prime == -1:
        print("NOT FOUND")
    else:
        print(max_prime)
        for i in range(n):
            for j in range(m):
                if a[i][j] == max_prime:
                    print("Vi tri ", '[', i, ']', '[', j, ']', sep = '')