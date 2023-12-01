a, b = [], [0] * 1000
n, k = map(int, input().split())

def in_ra():
    for i in range(k):
        print(a[b[i]], end = ' ')
    print()

def Try(i, bd):
    for j in range(bd, len(a) - k + i):
        b[i - 1] = j
        if i == k: in_ra()
        else: Try(i + 1, j + 1)

if __name__ == '__main__':
    a, se = input().split(), set()
    for item in a:
        se.add(item)
    a.clear()
    for item in sorted(se):
        a.append(item)
    Try(1, 0)
