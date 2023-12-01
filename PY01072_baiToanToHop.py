n, k = map(int, input().split())
a, ans = [int(x) for x in input().split()], [0] * 1001
se, check = set(a), True
n, a = len(se), []
a.append(0)
for x in se:
    a.append(x)
a.sort()

def in_ra():
    for i in range(1, k + 1):
        print(ans[i], end = ' ')
    print()

def Try(i, bd):
    for j in range(bd, n - k + i + 1):
        ans[i] = a[j]
        if i == k: in_ra()
        else: Try(i + 1, j + 1)

Try(1, 1)
# def sinh():
#     #global check
#     in_ra()
#     i = k
#     while i > 0 and ans[i] == n - k + i: i -= 1
#     if i == 0: check = False
#     else:
#         ans[i] += 1
#         for j in range(i + 1, k + 1):
#             ans[j] = ans[j - 1] + 1

# while check:
#     sinh()