t = int(input())
while t > 0:
    t -= 1
    s = input()
    ans = ''
    dem = 0
    i = 0
    tmp = s[0]
    while i < len(s):
        while i < len(s) and s[i] == tmp:
            dem += 1
            i += 1
        if i == len(s):
            ans += str(dem) + tmp
            break
        else:
            ans += str(dem) + tmp
            tmp = s[i]
            dem = 0
    print(ans)