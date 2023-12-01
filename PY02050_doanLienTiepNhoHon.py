t = int(input())
while t > 0:
    n = int(input())
    a, st = [int(x) for x in input().split()], []
    d = [0] * 100005
    a.insert(0, 0)
    for i in range(n, 0, -1):
        while len(st) > 0 and a[i] > a[st[len(st) - 1]]:
            d[st[len(st) - 1]] = i
            st.pop()
        st.append(i)
    for i in range(1, n + 1):
        if i == 0:
            print(1, end = ' ')
            continue
        if d[i] == i - 1: print(1, end = ' ')
        else: print(i - d[i], end = ' ')
    print()
    t -= 1