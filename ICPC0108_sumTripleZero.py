t = int(input())
for u in range(t):
    cnt = 0
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    for i in range(0, n - 2):
        l = i + 1
        r = len(a) - 1
        while l < r:
            if a[l] + a[i] + a[r] == 0:
                cnt += 1
                l += 1
            elif a[l] + a[i] + a[r] < 0:
                l += 1
            else: r -= 1
    print(cnt)