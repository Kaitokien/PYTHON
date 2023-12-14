from math import *
prime, b = [1] * 10007, []
prime[0], prime[1] = 0, 0
for i in range(2, isqrt(10007)):
    if prime[i] == 1:
        for j in range(i + i, 10007, i):
            prime[j] = 0
for i in range(10007):
    if prime[i] == 1:
        b.append(i)

n = int(input())
a = list(map(int, input().split()))
ans, res = 0, 99999999
for i in a:
    res = 99999999
    for j in b:
        res = min(res, abs(i - j))
    ans = max(ans, res)
print(ans)