def check(s):
    if s == s[::-1]: return True
    return False

with open("VANBAN.in") as in_put:
    line = in_put.read()
arr, do_dai = line.split(), -1
tu_dien, ans = dict(), []
for item in arr:
    if check(item) and len(item) >= do_dai:
        if tu_dien.get(item) == None:
            tu_dien[item] = 1
        else: tu_dien[item] += 1
        do_dai = len(item)
for keys in tu_dien:
    if len(keys) == do_dai:
        print(keys, tu_dien[keys])