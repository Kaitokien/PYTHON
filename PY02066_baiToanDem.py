n = int(input())
a, max_val, dem, check = [], -1, 0, True
while True:
    tmp = [int(x) for x in input().split()]
    a += tmp
    for item in tmp:
        max_val = max(max_val, item)
    dem += len(tmp)
    if dem == n:
        break
for i in range(1, max_val + 1):
    if i not in a:
        check = False
        print(i)
    
if check: print("Excellent!")