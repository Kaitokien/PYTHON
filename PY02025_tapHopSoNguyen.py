n, m = map(int, input().split())
se1, se2 = set(), set()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for item in a: se1.add(item)
for item in b: se2.add(item)
for item in sorted(se1):
    if item in sorted(se2):
        print(item, end = ' ')
print()
for item in sorted(se1):
    if item not in sorted(se2):
        print(item, end = ' ')
print()
for item in sorted(se2):
    if item not in sorted(se1):
        print(item, end = ' ')