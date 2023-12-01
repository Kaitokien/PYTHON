P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    string = input()
    if string[0] == '0':
        break
    k, s = map(str, string.split())
    ans = ""
    for i in range(len(s)):
        if str.isalpha(s[i]) == True:
            ans += P[(ord(s[i]) - 65 + int(k)) % 28]
        else:
            if s[i] == '_': ans += P[(26 + int(k)) % 28]
            else:
                ans += P[(27 + int(k)) % 28]
    ans = ans[::-1]
    print(ans)
