while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and a == b and b == c and c == d:
        break
    tong = 0
    while True:
        if a == b and b == c and c == d:
            break
        tmp = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - tmp)
        tong += 1
    print(tong)