t = int(input())
while t > 0:
    n = input()
    rev = n[::-1]
    check = True
    for i in range(1, len(n)):
        if int(abs(ord(n[i]) - ord(n[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1]))):
            check = False
            break
    if check == True:
        print("YES")    
    else:
        print("NO")
    t -= 1