str1 = int(input())
str2 = int(input())
str1 = str(str1)
str2 = str(str2)
if len(str1) > len(str2):
    t = str1
    str1 = str2
    str2 = t
xau = ''
str1 = str1[::-1]
str2 = str2[::-1]
nho = 0
for i in range(len(str1)):
    tong = (ord(str1[i]) - 48 + ord(str2[i]) - 48 + nho)
    xau += chr(tong % 10 + 48)
    nho = tong // 10

for i in range(len(str1), len(str2)):
    tong = (ord(str2[i]) - 48 + nho)
    xau += chr(tong % 10 + 48)
    nho = tong // 10
if nho:
    xau += chr(nho + 48)
xau = xau[::-1]
print(xau)