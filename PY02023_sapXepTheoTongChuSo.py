from math import *

def sum_of_digit(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        a.sort(key = sum_of_digit)
        for item in a:
            print(item, end = ' ')
        print()
    