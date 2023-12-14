t = int(input())
for _ in range(t):
    n, idx_1, idx_2 = input(), -1, 0
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            idx_1 = i
            break
    if idx_1 == -1: print(-1)
    else: 
        res, to, idx_2 = n[idx_1], n[idx_1 + 1], idx_1 + 1
        for i in range(idx_1 + 2, len(n)):
            if n[i] < res and n[i] > to:
                idx_2 = i
                to = n[i]
        n = n[:idx_1] + n[idx_2] + n[idx_1 + 1:idx_2] + n[idx_1] + n[idx_2 + 1:]
        if n[0] == '0': print(-1)
        else: print(''.join(n))