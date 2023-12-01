from math import *
sang = [1] * 1000005
def sieve():
    sang[0] = 0
    sang[1] = 0
    for i in range(2, isqrt(1000005) + 1):
        if sang[i] == 1:
            for j in range(i * i, 1000005, i):
                sang[j] = 0

if __name__ == '__main__':
    n, x = map(int, input().split())
    sieve()
    print(x, end = ' ')
    for i in range(1000006):
        if n == 0:
            break
        if sang[i] == 1:
            print(x + i, end = ' ')
            x += i
            n -= 1