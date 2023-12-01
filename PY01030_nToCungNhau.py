from math import *
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    if a == 1:
        return True
    return False

if __name__ == '__main__':
    n, k = map(int, input().split())
    dem = 0
    for i in range(int(pow(10, k - 1)), int(pow(10, k))):
        if dem == 10:
            print()
            dem = 0
        if gcd(i, n) == True:
            print(i, end = ' ')
            dem += 1