n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
if n == 2:
    print(a[0][1] // 2, a[0][1] // 2)
else:
    ans, tmp = [], (a[0][1] + a[0][2] - a[1][2]) // 2
    ans.append(tmp)
    for i in range(1, n):
        ans.append(a[0][i] - tmp)
    for item in ans:
        print(item, end = ' ')