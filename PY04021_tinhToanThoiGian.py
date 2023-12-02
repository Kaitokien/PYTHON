from datetime import datetime

class Gamer:
    def __init__(self, ma, hoTen, gioBD, gioKT):
        self.hoTen = hoTen
        self.ma = ma
        self.gioBD = gioBD
        self.gioKT = gioKT

    def tgianchoi(self):
        t1 = datetime.strptime(self.gioBD, "%H:%M")
        t2 = datetime.strptime(self.gioKT, "%H:%M")
        return (t2 - t1).seconds

    def soGio(self):
        t1 = datetime.strptime(self.gioBD, "%H:%M")
        t2 = datetime.strptime(self.gioKT, "%H:%M")
        tmp = (t2 - t1).seconds
        return tmp // 3600

    def soPhut(self):
        t1 = datetime.strptime(self.gioBD, "%H:%M")
        t2 = datetime.strptime(self.gioKT, "%H:%M")
        tmp = (t2 - t1).seconds
        tmp -= (tmp // 3600) * 3600
        return tmp // 60
    
    def __str__(self):
        gio = self.soGio()
        phut = self.soPhut()
        return "{} {} {} gio {} phut".format(self.ma, self.hoTen, gio, phut)
    
if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        ma = input()
        hoTen = input()
        gioBD = input()
        gioKT = input()
        gamer = Gamer(ma, hoTen, gioBD, gioKT)
        arr.append(gamer)
    arr.sort(key = lambda x : x.tgianchoi(), reverse = True)
    for item in arr:
        print(item)