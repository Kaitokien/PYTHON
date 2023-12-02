t = int(input())
for _ in range(t):
    n = input()
    if len(n) <= 100: print(n)
    else:
        arr = n.split()
        cnt = 0
        for item in arr:
            if cnt + len(item) > 100: break
            print(item, end = ' ')
            cnt += len(item) + 1
        print()