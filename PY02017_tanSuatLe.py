t = int(input())
while t > 0:
    tu_dien = {}
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    for item in a:
        if item not in tu_dien.keys():
            tu_dien[item] = 1
        else:
            tu_dien[item] += 1
    for key, value in tu_dien.items():
        if value % 2 == 1:
            print(key)
            break
