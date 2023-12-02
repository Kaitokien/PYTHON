from math import *

class MonHoc:
    def __init__(self, maMon, tenMon, hinhThucThi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThucThi = hinhThucThi
    
    def getMaMon(self):
        return self.maMon
    
    def __str__(self):
        return "{} {} {}".format(self.maMon, self.tenMon, self.hinhThucThi)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        maMon = input()
        tenMon = input()
        hinhThucThi = input()
        x = MonHoc(maMon, tenMon, hinhThucThi)
        arr.append(x)
    arr.sort(key = lambda x : x.getMaMon())
    for item in arr:
        print(item)
