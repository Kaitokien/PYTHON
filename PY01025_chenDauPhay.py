n = input()
xau = ""
dem = 0
for i in range(len(n) - 1, -1, -1):
    if dem == 3:
        xau += ','
        xau += n[i]
        dem = 1
    else:
        xau += n[i]
        dem += 1
xau = xau[::-1]
print(xau)