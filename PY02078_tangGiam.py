#Bài này sử dụng quy hoạch động: LIS

t = int(input())
for _ in range(t):
    a, b, n = [], [], int(input())
    mark = [1] * 505
    for i in range(n):
        x, y = map(float, input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                mark[i] = max(mark[i], mark[j] + 1)
    print(max(mark))    