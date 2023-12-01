n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
min_val, idx, ans = 9999999999, 0, -1
while idx < len(a):
    distance = 0
    for i in range(len(a)):
        distance += abs(a[idx] - a[i])
    if distance < min_val:
        min_val = distance
        ans = a[idx]
    idx += 1
print(min_val, ans)