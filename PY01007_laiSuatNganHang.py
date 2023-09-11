t = int(input())
while t > 0:
    t -= 1
    n, x, m = map(float, input().split())
    year = 0
    while n < m:
        profit = n * (x / 100)
        n += profit
        year += 1
    print(year)