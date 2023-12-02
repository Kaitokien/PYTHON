import sys

save, ans= [], []
for line in sys.stdin:
    for var in line.split():
        save.append(var.lower())

in_hoa, cau = True, ''
for word in save:
    if in_hoa == True:
        word = word.title()
        in_hoa = False
        if len(cau) > 0: 
            ans.append(cau[:len(cau) - 1])
            cau = ''
    if word.count('.') > 0 or word.count('?') > 0 or word.count('!') > 0 or word == '.' or word == '?' or word == '!':
        in_hoa = True
        word = word.replace('.', '')
        word = word.replace('?', '')
        word = word.replace('!', '')
    cau += word + " "
if len(cau) > 0:
    ans.append(cau)
for item in ans:
    print(item)