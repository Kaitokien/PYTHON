t = int(input())
while t > 0:
    n, d = map(int, input().split())
    a = [int(x) for x in input().split()]
    while d > 0:
        d -= 1
        tmp = a[0]
        a.pop(0)
        a.append(tmp)
    for i in range(n):
        print(a[i], end = ' ')
    print()
    t -= 1