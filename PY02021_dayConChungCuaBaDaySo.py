t = int(input())
while t > 0:
    t -= 1
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    idx_1, idx_2, d = 0, 0, []
    while idx_1 < len(a) and idx_2 < len(b):
        if a[idx_1]  == b[idx_2]:
            d.append(a[idx_1])
            idx_1 += 1
            idx_2 += 1
        else:
            if a[idx_1] > b[idx_2]:
                idx_2 += 1
            else: idx_1 += 1
    if len(d) == 0: print("NO")
    else:
        idx_3, idx_4, ans = 0, 0, []
        while idx_3 < len(c) and idx_4 < len(d):
            if c[idx_3]  == d[idx_4]:
                ans.append(c[idx_3])
                idx_3 += 1
                idx_4 += 1
            else:
                if c[idx_3] > d[idx_4]:
                    idx_4 += 1
                else: idx_3 += 1
        if len(ans) == 0: print("NO")
        else:
            for item in ans:
                print(item, end = ' ')
            print()