from sys import *
def std_gen():
    for u in stdin.read().split():
        yield int(u)
cin = std_gen()

setrecursionlimit(pow(10, 8))
n, m, s = next(cin), next(cin), next(cin)
ke = [[] for _ in range(n + 2)]
for i in range(m):
    x, y = next(cin), next(cin)
    ke[x].append(y)
    ke[y].append(x)
visited, tplt, cnt, res = [0] * 100005, [0] * 100005, 0, True
def DFS(u):
    visited[u] = 1
    tplt[u] = cnt
    for v in ke[u]:
        if not visited[v]:
            DFS(v)
for vertex in range(1, n + 1):
    if not visited[vertex]:
        cnt += 1
        DFS(vertex)
for vertex in range(1, n + 1):
    if vertex == s: continue
    if tplt[vertex] != tplt[s]:
        res = False
        print(vertex)
if res: print(0)