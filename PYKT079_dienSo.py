t = int(input())
while t > 0:
    mark = [0] * 1005
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    l, r, cnt = min(a), max(a), 0
    for item in a:
        mark[item] = 1
    for i in range(l, r + 1):
        if mark[i] == 0: cnt += 1
    print(cnt)