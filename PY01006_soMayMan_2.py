t = int(input())
while t > 0:
    str = input()
    check = True
    for i in range(len(str)):
        if(str[i] != '4' and str[i] != '7'):
            print("NO")
            check = False
            break;
    if check == True:
        print("YES")
    t -= 1