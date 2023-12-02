t = int(input())
while t > 0:
    t -= 1
    s, ans, i, tmp = input(), -1, 0, -1
    while i < len(s):
        tmp = -1
        if s[i].isdigit(): tmp = 0
        while(i < len(s) and s[i].isdigit()):
            tmp = tmp * 10 + int(s[i])
            i += 1
        if tmp != -1: ans = max(ans, tmp)
        i += 1
    if tmp != -1: ans = max(ans, tmp)
    print(ans)