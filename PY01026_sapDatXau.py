from math import *

t = int(input())
for i in range(1, t + 1):
    s1 = input()
    s2 = input()
    a = list(s1)
    b = list(s2)
    a.sort()
    b.sort()
    print("Test " + str(i) + ": ", end = '')
    if a == b:
        print("YES")
    else: print("NO")