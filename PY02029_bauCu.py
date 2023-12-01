n, m = map(int, input().split())
a = list(map(int, input().split()))
tu_dien, se, max_val, ans = {}, set(), 0, -1
for item in a:
    if item not in tu_dien.keys():
        tu_dien[item] = 1
    else: tu_dien[item] += 1
    max_val = max(max_val, tu_dien[item])
for item in a:
    se.add(tu_dien[item])
if len(se) == 1: print("NONE")
else:
    res = 0
    for item in a:
        if tu_dien[item] != max_val and tu_dien[item] > res:
            res = tu_dien[item]
            ans = item
    print(ans)