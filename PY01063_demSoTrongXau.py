
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        m = input()
        cnt, res = 0, n.find(m)
        while res != -1:
            cnt += 1
            res = n.find(m, len(m) + res)
        print(cnt)
        t -= 1