from math import *

t = int(input())
while t > 0:
    t -= 1
    n, b = map(int, input().split())
    ans = ""
    while n > 0:
        du = n % b
        if du < 10:
            ans += str(du)
        else:
            ans += chr(du + 55)
        n //= b
    ans = ans[::-1]
    print(ans)