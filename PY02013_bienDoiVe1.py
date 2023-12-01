while True:
    n = int(input())
    if n == 0:
        break
    tong = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            tong += 1
        else:
            n = n * 3 + 1
            tong += 1
    print(tong)