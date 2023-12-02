n = int(input())
check, cnt, title = False, 0, ''
tu_dien = dict()
while n > 0:
    s = input()
    if len(s) == 0:
        check = False
        tu_dien[title] = cnt
        cnt, title = 0, ''
    elif check == False:
        title = s + ':'
        check = True
    else: cnt += 1
    n -= 1
if title != '':
    tu_dien[title] = cnt
for x in tu_dien:
    print(x, tu_dien[x])