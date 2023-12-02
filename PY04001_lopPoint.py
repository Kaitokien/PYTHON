from math import *

class Point:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
    
    def distance(self, other):
        ans = sqrt((abs(self.__p1 - other.__p1)) ** 2 + (abs(self.__p2 - other.__p2)) ** 2)
        return '{:.4f}'.format(ans)

def Decimal(x):
    return float(x)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1