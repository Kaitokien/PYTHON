s = input()
while len(s) > 1:
    mid = len(s) // 2
    dau = s[0:mid]
    cuoi = s[mid:]
    s = str(int(dau) + int(cuoi))
    print(s)