t = int(input())
while t > 0:
    t -= 1
    n = input()
    rev_n = n[::-1]
    check = True
    for i in range(1, len(n)):
        if abs(ord(n[i]) - ord(n[i - 1])) != abs(ord(rev_n[i]) - ord(rev_n[i - 1])):
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")