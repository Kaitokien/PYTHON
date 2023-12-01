t = int(input())
while t > 0:
    t -= 1
    s = input()
    tong = 0
    tich = 1
    for i in range(0, len(s)):
        if i % 2 == 1:
            tong += int(s[i])
        else:
            if s[i] != '0':
                tich *= int(s[i])
    print(tich, tong)