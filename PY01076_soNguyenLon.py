from math import *

def modulo(a, b):
    mod = 0
    for i in range(len(b)):
        mod = (mod * 10 + ord(b[i])) % a
    return mod


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        m = int(input())
        print(gcd(n, m))
        t -= 1