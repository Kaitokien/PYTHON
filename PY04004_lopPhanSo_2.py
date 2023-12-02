from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau

    def __add__(self, other):
        up = self.__tu * other.__mau + self.__mau * other.__tu
        down = self.__mau * other.__mau
        tmp = gcd(up, down)
        up //= tmp
        down //= tmp
        return PhanSo(up, down)
    
    def __str__(self):
        return f'{self.__tu}/{self.__mau}'

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    p = PhanSo(a, b)
    q = PhanSo(c, d)
    ans = p + q
    print(ans)