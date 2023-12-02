n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
C = [[0 for _ in range(200)] for _ in range(200)]
for i in range(1, 200):
    for j in range(200):
        if j == 0 or i == j:
            C[i][j] = 1
        else: C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
for i in range(n):
    a[i] = list(input())
ans = 0
for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C': dem += 1
    if dem < 2: continue
    ans += C[dem][2]
for j in range(n):
    dem = 0
    for i in range(n):
        if a[i][j] == 'C': dem += 1
    if dem < 2: continue
    ans += C[dem][2]
print(ans)
