def tongchuso(n):
    ans = 0
    while n > 0:
        r = n % 10
        ans += r
        n //= 10
    if ans % 10 != 0:
        return False
    return True

t = int(input())
while t > 0:
    n = input()
    if tongchuso(int(n)) == True:
        check = True
        for i in range(len(n) - 1):
            if abs(int(n[i]) - int(n[i + 1])) != 2:
                check = False
                print("NO")
                break
        if check == True:
            print("YES")
    else:
        print("NO")
    t -= 1