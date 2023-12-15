n, tu_dien, ans, word = input(), dict(), [], ''
for _ in range(int(n)):
    line = input().lower()
    for c in line + " ":
        if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
            word += c
        else:
            if word != '':
                if word not in tu_dien:
                    tu_dien[word] = 1
                else: tu_dien[word] += 1
                word = ''
for key in tu_dien:
    ans.append([key, tu_dien[key]])
ans.sort(key=lambda x : (-x[1], x[0]))
for item in ans:
    print(item[0], item[1])