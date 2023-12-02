t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    res, idx = max(a), -1
    for i in range(len(a)):
        if a[i] == res:
            idx = i
            break
    a.insert(idx, m)
    b = [x for x in a if x < 0]
    for item in b:
        print(item, end = ' ')
    for item in a:
        if item >= 0:
            print(item, end = ' ')
    print()