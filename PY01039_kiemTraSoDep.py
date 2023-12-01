t = int(input())
while t > 0:
    t -= 1
    n = input()
    if n[0] == n[1]:
        print("NO")
        continue
    a = n[0]
    b = n[1]
    check = True
    for i in range(0, len(n)):
        if i % 2 == 0:
            if n[i] != a:
                check = False
                break
        elif i % 2 == 1:
            if n[i] != b:
                check = False
                break
    if check == True:
        print("YES")
    else:
        print("NO")