with open("DATA.in") as in_put:
    line = in_put.read()
arr, ans = line.split(), []
for item in arr:
    if item.strip().isdigit():
        if isinstance(int(item.strip()), int) == False:
            ans.append(item)
        else:
            if len(item) > 9: ans.append(item)
    else: ans.append(item)
ans.sort()
for item in ans:
    print(item, end = ' ')        
