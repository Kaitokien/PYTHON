n = int(input())
mark = [0] * 30005
a = list(map(int, input().split()))
for item in a:
    mark[item] = 1
check = True
for i in range(1, len(mark)):
    if mark[i] == 0:
        print(i)
        check = False
        break
if check == True:
    print(n + 1)