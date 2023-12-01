from math import *

s1 = input()
s2 = input()
pos = int(input())
ans = ''
ans += s1[:pos - 1] + s2 + s1[pos - 1:]
print(ans)