from math import *

class Point:
    def __init__(self, x, y):
        self.__p1 = x
        self.__p2 = y
    
    def distance(self, other):
        ans = sqrt((abs(self.__p1 - other.__p1)) ** 2 + (abs(self.__p2 - other.__p2)) ** 2)
        return ans

def Decimal(x):
    return float(x)

class Triangle:
    def __init__(self, P1, P2, P3):
        self.__P1 = P1
        self.__P2 = P2
        self.__P3 = P3

    def check(self):
        a = self.__P1.distance(self.__P2)
        b = self.__P1.distance(self.__P3)
        c = self.__P2.distance(self.__P3)
        if max(a, b, c) * 2 >= a + b + c:
            return False
        return True
    
    def parameter(self):
        a = self.__P1.distance(self.__P2)
        b = self.__P1.distance(self.__P3)
        c = self.__P2.distance(self.__P3)
        print('%.3f' % (a + b + c))
        

if __name__ == '__main__':
    t, arr, i = int(input()), [], 0
    for _ in range(t):
        arr += [float(i) for i in  input().split()]
    for _ in range(t):
        tam_giac = Triangle(Point(arr[i], arr[i + 1]), Point(arr[i + 2], arr[i + 3]), Point(arr[i + 4], arr[i + 5]))
        if tam_giac.check() == False:
            print("INVALID")
        else:
            tam_giac.parameter()
        i += 6