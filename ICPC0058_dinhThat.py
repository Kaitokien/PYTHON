# Đỉnh thắt là đỉnh mà tất cả đường đi từ u tới v đều đi qua nó

from sys import *
setrecursionlimit(pow(10, 8))
def stdin_gen():
    for x in stdin.read().split():
        yield int(x)
cin = stdin_gen()

t = next(cin)
for _ in range(t):
    n, m, u, v = next(cin), next(cin), next(cin), next(cin)
    ke, visited, dem = [[] for _ in range(n + 2)], [0] * 102, 0
    for i in range(m):
        x, y = next(cin), next(cin)
        ke[x].append(y)
    def DFS(u):
        visited[u] = 1
        for v in ke[u]:
            if not visited[v]:
                DFS(v)
    for i in range(1, n + 1):
        if i == u or i == v: continue
        visited = [0] * 102
        visited[i] = 1
        DFS(u)
        if not visited[v]: dem += 1
    print(dem)