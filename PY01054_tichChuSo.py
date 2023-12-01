t = int(input())
while t > 0:
    n = input()
    ans = 1
    for i in range(len(n)):
        if n[i] == '0':
            continue
        else:
            ans *= int(n[i])
    print(ans)
    t -= 1
