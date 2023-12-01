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
    t = int(input())
    while t > 0:
        n = input()
        m = n[::-1]
        a = int(n)
        b = int(m)
        if gcd(a, b) == True:
            print("YES")
        else:
            print("NO")
        t -= 1