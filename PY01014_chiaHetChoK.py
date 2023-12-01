a, k, n = map(int, input().split())
check = True
for i in range(1, int(n / k) + 1):
    if i * k - a > 0:
        check = False
        print(i * k - a, end = ' ')
if check == True:
    print(-1)