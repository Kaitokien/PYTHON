t = int(input())
F = [0] * 100
F[0] = 0
F[1] = 1
for i in range(2, 93):
    F[i] = F[i - 1] + F[i - 2]
while t > 0:
    t -= 1
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(F[i], end = ' ')
    print()