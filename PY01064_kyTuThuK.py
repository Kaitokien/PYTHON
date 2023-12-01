mark = [0] * 30

def init():
    mark[1] = 1
    for i in range(2, 26):
        mark[i] = mark[i - 1] + 2 ** (i - 1)

def kytu(n, k):
    if n == 1:
        return 'A'
    if k < mark[n] // 2 + 1:
        return kytu(n - 1, k)
    elif k > mark[n] // 2 + 1:
        return kytu(n - 1, k - mark[n - 1] - 1)
    else:
        tmp = chr(64 + n)
        return tmp

if __name__ == '__main__':
    t = int(input())
    init()
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        print(kytu(n, k))
