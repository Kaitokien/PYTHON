t = int(input())
while t > 0:
    tong = 0
    str = input()
    for i in range(len(str)):
        tong += int(str[i])
    if tong % 3 == 0:
        print("YES")
    else:
        print("NO")
    t -= 1