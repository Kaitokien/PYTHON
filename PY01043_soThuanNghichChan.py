def ktra(n):
    if len(n) % 2 == 1 or n != n[::-1]:
        return False
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = input()
        for i in range(22, int(n), 2):
            if ktra(str(i)) == True:
                print(i, end = ' ')
        print()
        t -= 1