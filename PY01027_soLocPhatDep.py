from math import *

s = input()
idx = 0
check = True
while idx < len(s):
    if idx == len(s) - 1:
        if s[idx] != '6': check = False
        break
    if s[idx] == '6':
        if idx + 2 < len(s):
            if (s[idx + 1] != '6' and s[idx + 1] != '8') or (s[idx + 2] != '6' and s[idx + 2] != '8'):
                check = False
                break
            if s[idx + 1] == '8' and s[idx + 2] == '8':
                idx += 3
            elif s[idx + 1] == '8' and s[idx + 2] == '6':
                idx += 2
            elif s[idx + 1] == '6':
                idx += 1
        elif idx + 1 < len(s):
            if s[idx + 1] != '6' and s[idx + 1] != '8':
                check = False
                break
            idx += 2
    else:
        check = False
        break
if check:
    print("YES")
else:
    print("NO")