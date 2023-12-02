def check(s):
    half = len(s) // 2
    if len(s) % 2 == 0:
        a, b = s[:half], s[half:]
        if a == b[::-1]:
            return True
        else: return False
    else:
        a, b = s[:half], s[half + 1:]
        if a == b[::-1]:
            return True
        else: return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    to = -1
    for i in range(n):
        for j in range(m):
            if len(str(a[i][j])) > 1 and check(str(a[i][j])) and to < a[i][j]:
                to = a[i][j]
    if to == -1:
        print("NOT FOUND")
    else:
        print(to)
        for i in range(n):
            for j in range(m):
                if a[i][j] == to:
                    print("Vi tri ", '[', i, ']', '[', j, ']', sep = '')