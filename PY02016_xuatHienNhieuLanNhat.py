t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    mark = [0] * 1000005
    a = list(map(int, input().split()))
    res = -1
    for item in a:
        mark[item] += 1
        res = max(res, mark[item])
    if res <= n // 2:
        print("NO")
    else:
        for i in range(len(mark)):
            if mark[i] == res:
                print(i)
                break
