from math import *

s = input()
ans = ''
dem = 0
tong = 0
for i in range(len(s) - 1, -1, -1):
    if dem == 3:
        dem = 0
        ans += str(tong)
        tong = 0
    if s[i] == '1':
        tong += 2 ** dem
    dem += 1
if tong > 0:
    ans += str(tong)
ans = ans[::-1] 
print(ans)