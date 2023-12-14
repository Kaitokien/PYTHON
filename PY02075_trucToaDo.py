class Line:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
t = int(input())
for _ in range(t):
    n, arr, cnt = int(input()), [], 1
    for i in range(n):
        x, y = map(int, input().split())
        line = Line(x, y)
        arr.append(line)
    arr.sort(key = lambda x : x.stop)
    res = arr[0].stop
    for i in range(1, len(arr)):
        if res <= arr[i].start:
            cnt += 1
            res = arr[i].stop
    print(cnt)