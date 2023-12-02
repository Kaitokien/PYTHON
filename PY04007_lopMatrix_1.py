from math import *

class Matrix:
    def __init__(self, n, m, mt):
        self.__n = n
        self.__m = m
        self.__mt = mt

    def __mul__(self):
        tmp = []
        for i in range(self.__n):
            tmp += [[0] * self.__n]
            for j in range(self.__n):
                for k in range(self.__m):
                    tmp[i][j] += self.__mt[i][k] * self.__mt[j][k]
        return Matrix(self.__n, self.__m, tmp)
    
    def __str__(self):
        for i in self.__mt:
            print(*i)    
        return ''

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        mt = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            mt[i] = list(map(int, input().split()))
        a = Matrix(n, m, mt)
        print(a.__mul__(), end = '')