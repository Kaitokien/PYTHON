t = int(input())
while t > 0:
    t -= 1
    n = input()
    if len(n) % 2 != 1 or n[0] == n[1]:
        print("NO")
    else:
        res = int(n[0])
        check = True
        for i in range(0, len(n), 2):
            if int(n[i]) != res:
                check = False
                break
        if check == True:
            print("YES")
        else:
            print("NO")