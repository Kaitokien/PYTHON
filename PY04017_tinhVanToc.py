from datetime import datetime
from math import *

class Racer:
    def __init__(self, hoTen, donVi, vedich):
        self.hoTen = hoTen
        self.donVi = donVi
        self.vedich = vedich
        self.ma = ''
        a = (donVi + " " + hoTen).split()
        for item in a:
            self.ma += item[0]
    
    def tinhVTTB(self):
        t1 = datetime.strptime(self.vedich, "%H:%M")
        t2 = datetime.strptime("6:00", "%H:%M")
        hour = (t1 - t2).seconds / 3600
        return 120 / hour
    
    def __str__(self):
        vt_tb = self.tinhVTTB()
        return "{} {} {} {} Km/h".format(self.ma, self.hoTen, self.donVi, round(vt_tb))

if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        hoTen = input()
        donVi = input()
        vedich = input()
        x = Racer(hoTen, donVi, vedich)
        arr.append(x)
    arr.sort(key = lambda x : x.vedich)
    for item in arr:
        print(item)
