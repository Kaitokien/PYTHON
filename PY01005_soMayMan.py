str = input()
check = True
num = 0
for i in range(len(str)):
    if(str[i] == '4' or str[i] == '7'):
        num += 1
if num == 4 or num == 7:
    print("YES")
else:
    print("NO")