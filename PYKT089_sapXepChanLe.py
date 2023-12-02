n = int(input())
a = list(map(int, input().split()))
chan, le, idx1, idx2 = [], [], 0, 0
for x in a:
    if x % 2 == 0: chan.append(x)
    else: le.append(x)
chan.sort()
le.sort(reverse=True)
for i in range(len(a)):
    if x % 2 == 0:
        print(le[idx1], end = ' ')
        idx1 += 1
    else:
        print(chan[idx2], end = ' ')
        idx2 += 1