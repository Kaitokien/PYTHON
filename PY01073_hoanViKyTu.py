# used = [0] * 300
# s = input()

# def Try(ans, i):
#     if i == len(s):
#         print(ans)
#         return
#     for j in range(len(s)):
#         if used[j] == 0:
#             used[j] = 1
#             Try(ans + s[j], i + 1)
#             used[j] = 0

# Try('', 0)
used, a = [0] * 300, ['a'] * 10
s = input()

def in_ra():
    for i in range(len(s)):
        print(a[i], end = '')
    print()

def Try(i):
    for j in range(len(s)):
        if used[j] == 0:
            a[i] = s[j]
            used[j] = 1
            if i == len(s) - 1:
                in_ra()
            else: Try(i + 1)
            used[j] = 0

Try(0)