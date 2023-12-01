t = int(input())
while t > 0:
    t -= 1
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    check = True
    for i in range(len(a)):
        if a[i] > b[i]:
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")