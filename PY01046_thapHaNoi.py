def thap(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    thap(n - 1, a, c, b)
    print(a, "->", c)
    thap(n - 1, b, a, c)
    
if __name__ == '__main__':
    n = int(input())
    a, b, c = 'A', 'B', 'C'
    thap(n, a, b, c)