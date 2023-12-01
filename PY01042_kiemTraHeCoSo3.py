t = int(input())
while t > 0:
    t -= 1
    n = input()
    check = True
    for i in range(len(n)):
        if n[i] != '0' and n[i] != '1' and n[i] != '2':
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")