def giaithua(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, ans = input(), 0
        for i in range(len(n)):
            ans += giaithua(int(n[i]))
        if ans == int(n):
            print("Yes")
        else: print("No")