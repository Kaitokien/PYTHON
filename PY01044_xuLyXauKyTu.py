n = [i for i in input().lower().split()]
m = [i for i in input().lower().split()]
hop = set()
tu_dien = {}
for item in n:
    hop.add(item)
for item in m:
    hop.add(item)
for item in sorted(hop):
    print(item, end = ' ')
print()
for item in sorted(n):
    if m.count(item) and item not in tu_dien.keys():
        print(item, end = ' ')
        tu_dien[item] = 1