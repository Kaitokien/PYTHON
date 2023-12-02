from math import *

n = input()
idx = len(n) - 1
cnt = 0
dem = 0
ans = ""
while idx >= 0:
    if cnt == 3:
        ans += str(dem)
        dem = 0
        cnt = 0
    if n[idx] == '0':
        cnt += 1
        idx -= 1
        continue
    elif n[idx] == '1':
        dem += 2 ** cnt
        cnt += 1
    idx -= 1
if dem != 0:
    ans += str(dem)
ans = ans[::-1]
print(ans)