from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        check = True
        for i in range(len(n)):
            if nt(i) == False:
                if n[i] == '2' or n[i] == '3' or n[i] == '5' or n[i] == '7':
                    check = False
                    break
            else:
                if n[i] != '2' and n[i] != '3' and n[i] != '5' and n[i] != '7':
                    check = False
                    break
        if check == True:
            print("YES")
        else:
            print("NO")