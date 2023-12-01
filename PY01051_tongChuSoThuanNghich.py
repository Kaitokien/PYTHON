t = int(input())
while t > 0:
    t -= 1
    ans = 0
    n = input()
    for i in range(len(n)):
        ans += int(n[i])
    if len(str(ans)) < 2:
        print("NO")
    else:
        rev_ans = str(ans)[::-1]
        if str(ans) != rev_ans:
            print("NO")
        else:
            print("YES")