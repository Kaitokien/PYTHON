from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        p, q = map(int, input().split())
        x1 = input().strip()
        if x1.count(' '): x1, x2 = x1.split()
        else: x2 = input()
        x1 = x1.replace(str(max(p, q)), str(min(p, q)))
        x2 = x2.replace(str(max(p, q)), str(min(p, q)))
        print(int(x1) + int(x2), end = ' ')
        x1 = x1.replace(str(min(p, q)), str(max(p, q)))
        x2 = x2.replace(str(min(p, q)), str(max(p, q)))
        print(int(x1) + int(x2))
        t -= 1