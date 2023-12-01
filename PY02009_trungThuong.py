t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    mark = [0] * 1005
    to = -1
    while n > 0:
        n -= 1
        u = int(input())
        mark[u] += 1
        to = max(to, mark[u])
    for i in range(1, 1001):
        if mark[i] == to:
            print(i)
            break