from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    
    def __str__(self):
        res = gcd(self.__tu, self.__mau)
        self.__tu //= res
        self.__mau //= res
        return f'{self.__tu}/{self.__mau}'

if __name__ == '__main__':
    a, b = map(int, input().split())
    p = PhanSo(a, b)
    print(p)