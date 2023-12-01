while True:
    n = int(input())
    if n == 0: break
    a = [int(input()) for i in range(n)]
    if a.count(a[0]) == n:
        print("BANG NHAU")
    else:
        print(min(a), max(a))