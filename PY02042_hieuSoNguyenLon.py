str1 = int(input())
str2 = int(input())
str1 = str(str1)
str2 = str(str2)
check = True
if int(str1) < int(str2):
    check = False
    t = str1
    str1 = str2
    str2 = t
str1 = str1[::-1]
str2 = str2[::-1]
nho = 0
xau = ''
for i in range(len(str2)):
    if ord(str1[i]) - 48 - nho >= ord(str2[i]) - 48:
        hieu = (ord(str1[i]) - 48) - (ord(str2[i]) - 48) - nho
        xau += chr(hieu + 48)
        nho = 0
    else:
        hieu = (ord(str1[i]) - 48 + 10) - (ord(str2[i]) - 48) - nho
        xau += chr(hieu + 48)
        nho = 1
for i in range(len(str2), len(str1)):
    if ord(str1[i]) - 48 - nho >= 0:
        hieu = (ord(str1[i]) - 48) - nho
        xau += chr(hieu + 48)
        nho = 0
    else:
        hieu = (ord(str1[i]) - 48 + 10) - nho
        xau += chr(hieu + 48)
        nho = 1
xau = xau[::-1]
xau = int(xau)
xau = str(xau)
if int(xau) == 0:
    print(0)
elif check == False:
    xau = '-' + xau
    print(xau)
elif check:
    print(xau)