from math import *

t = int(input())
while t > 0:
    t -= 1
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i].isdigit():
            ans += int(s[i])
    res = sorted(s)
    for i in range(len(res)):
        if res[i].isdigit() == False:
            print(res[i], end = "")
    print(ans)