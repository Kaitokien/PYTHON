t = int(input())
for _ in range(t):
    s = input()
    stack = []
    tu_dien, cnt = dict(), 1
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
            tu_dien[i] = cnt
            cnt += 1
        elif s[i] == ')':
            res = stack[len(stack) - 1]
            tu_dien[i] = tu_dien[res]
            stack.pop()
    for k in tu_dien.values():
        print(k, end = ' ')
    print()
