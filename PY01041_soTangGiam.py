t = int(input())
while t > 0:
    t -= 1
    n = input()
    if len(n) < 3:
        print("NO")
    else:
        idx = -1
        check = True
        for i in range(0, len(n) - 1):
            if n[i] == n[i + 1]:
                check = False
                break
            elif int(n[i]) > int(n[i + 1]):
                if i > 0:
                    idx = i
                break
        if check == False or idx == -1:
            print("NO")
        else:
            for i in range(idx, len(n) - 1):
                if int(n[i]) <= int(n[i + 1]):
                    check = False
                    break
            if check == True:
                print("YES")
            else:
                print("NO")