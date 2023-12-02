with open("DATA.in") as in_put:
    line = in_put.readlines()
t, idx = int(line[0].strip()), 1
for _ in range(t):
    b, ans = int(line[idx].strip()), ''
    idx += 1
    s = line[idx].strip()
    idx += 1
    if b == 2: print(s)
    elif b == 4:
        s = s[::-1]
        i, mu, res = 0, 0, 0
        while i < len(s):
            if mu == 2:
                ans += str(res)
                res = 0
                mu = 0
            res += int(s[i]) * (2 ** mu)
            mu += 1
            i += 1
        if res != 0: ans += str(res)
        ans = ans[::-1]
        print(ans)
    elif b == 8:
        s = s[::-1]
        i, mu, res = 0, 0, 0
        while i < len(s):
            if mu == 3:
                ans += str(res)
                res = 0
                mu = 0
            res += int(s[i]) * (2 ** mu)
            mu += 1
            i += 1
        if res != 0: ans += str(res)
        ans = ans[::-1]
        print(ans)
    elif b == 16:
        s = s[::-1]
        i, mu, res = 0, 0, 0
        while i < len(s):
            if mu == 4:
                if res < 10: ans += str(res)
                else:
                    ans += chr(55 + res)
                res = 0
                mu = 0
            res += int(s[i]) * (2 ** mu)
            mu += 1
            i += 1
        if res != 0:
            if res < 10: ans += str(res)
            else:
                ans += chr(55 + res)
        ans = ans[::-1]
        print(ans)