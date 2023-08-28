t = int(input())
while t > 0:
    n = input()
    if len(n) < 2:
        print(n)
    else:
        i, nho, ans = len(n) - 1, 0, ""
        while i > 0:
            tmp = int(n[i]) + nho
            if tmp >= 5:
                nho = 1
            else:
                nho = 0
            ans = '0' + ans
            i -= 1
        ans = str(int(n[i]) + nho) + ans
        print(ans)
    t -= 1
    