t = int(input())
while t > 0:
    n = input()
    if len(n) == 1:
        print("NO")
    elif n[len(n) - 1] == '6' and n[len(n) - 2] == '8':
        print("YES")
    else:
        print("NO")
    t -= 1