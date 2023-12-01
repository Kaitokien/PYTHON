t = int(input())

while t > 0:
    t -= 1
    n = input()
    check = True
    for i in range(0, len(n) - 1):
        if int(n[i]) - int(n[i + 1]) > 0:
            check = False
            break;
    if check == True:
        print("YES")
    else:
        print("NO")