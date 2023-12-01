from math import *

def times_of_digit(n):
    tich = 1
    while n > 0:
        tich *= n % 10
        n //= 10
    return tich

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        a.sort(key = times_of_digit)
        for item in a:
            print(item, end = ' ')
        print()
    