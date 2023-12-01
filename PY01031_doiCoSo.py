from math import *

t = int(input())
while t > 0:
    t -= 1
    n, b = map(int, input().split())
    ans = ''
    while n > 0:
        r = n % b
        if r < 10: ans += str(r)
        else: ans += chr(r + 55)
        n //= b
    ans = ans[::-1]
    print(ans)