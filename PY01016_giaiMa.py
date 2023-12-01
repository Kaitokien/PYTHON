t = int(input())
while t > 0:
    t -= 1
    n = input()
    xau = ''
    for i in range(0, len(n) - 1, 2):
        tmp = int(n[i + 1]) * n[i]
        xau += tmp
    print(xau)