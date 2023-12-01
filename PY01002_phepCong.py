n = input()
a = n.split()
tmp = 0
tmp += int(a[0]) + int(a[2])
tong = int(a[4])
if(tmp == tong):
    print("YES")
else:
    print("NO")   