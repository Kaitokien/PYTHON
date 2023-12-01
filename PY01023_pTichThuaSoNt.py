from math import *

def ptich(n):
    print("1 * ", end = '')
    check = False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                n /= i
                mu += 1
            print(i, mu, sep = '^', end = '')
            if n > 1:
                print(' * ', end = '')
    if n > 1:
        check = True
        print(int(n), 1, sep = '^')
    if check == False:
        print()
            
            

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        ptich(n)