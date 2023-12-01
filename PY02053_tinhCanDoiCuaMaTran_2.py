n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
tren = 0
duoi = 0
for i in range(n):
    for j in range(n):
        if i == n - 1 - j:
            continue
        elif i < n - j - 1:
            tren += a[i][j]
        else: duoi += a[i][j]
if abs(tren - duoi) <= k:
    print("YES")
    print(abs(tren - duoi))
else:
    print("NO")
    print(abs(tren - duoi))