n, ans = int(input()), 0
a = ["" for _ in range(n)]
for i in range(n):
    a[i] = input()
for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C': dem += 1
    if dem < 2: continue
    else: ans += dem * (dem - 1) // 2

for j in range(n):
    dem = 0
    for i in range(n):
        if a[i][j] == 'C': dem += 1
    if dem < 2: continue
    else: ans += dem * (dem - 1) // 2
print(ans)