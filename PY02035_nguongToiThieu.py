s, k, idx, check = input(), int(input()), 0, False
tu_dien = {}
while idx < len(s):
    xau = str(s[idx : idx + 2])
    if len(xau) < 2: break
    if xau in tu_dien:
        tu_dien[xau] += 1
    else: tu_dien[xau] = 1
    idx += 2
a = list(tu_dien.keys())
a.sort()
for item in a:
    if tu_dien[item] >= k:
        check = True
        print(item, tu_dien[item])
if check == False: print("NOT FOUND")