t = int(input())
while t > 0:
    t -= 1
    n = input()
    loop = 0
    tong = int(n)
    while loop <= 1000:
        if tong % 7 == 0:
            print(tong)
            break
        loop += 1
        tong += int(str(tong)[::-1])
    if loop > 1000:
        print(-1)