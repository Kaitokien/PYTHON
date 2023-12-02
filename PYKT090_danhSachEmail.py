with open("CONTACT.in") as in_put:
    line = in_put.readlines()
se, arr = set(), []
for item in line:
    s = item.strip().lower()
    if s not in se:
        arr.append(s)
        se.add(s)
arr.sort()
for item in arr:
    print(item)
in_put.close()