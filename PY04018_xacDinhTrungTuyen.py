from math import *

class GiaoVien:
    def __init__(self, maGV, hoTen, maXT, diemTin, diemCM):
        self.hoTen = hoTen
        self.maGV = "GV" + "{:02d}".format(maGV)
        self.maXT = maXT
        self.diemTin = diemTin
        self.diemCM = diemCM
        self.trangThai = ''
    
    def tinhDiem(self):
        diem = self.diemTin * 2 + self.diemCM
        if self.maXT[1] == '1': diem += 2
        elif self.maXT[1] == '2': diem += 1.5
        elif self.maXT[1] == '3': diem += 1
        return diem
    
    def __str__(self):
        diem = self.tinhDiem()
        if diem >= 18: self.trangThai = 'TRUNG TUYEN'
        else: self.trangThai = "LOAI"
        chuyen_mon = ''
        if self.maXT[0] == 'A': chuyen_mon = 'TOAN'
        elif self.maXT[0] == 'B': chuyen_mon = 'LY'
        else: chuyen_mon = 'HOA'
        return "{} {} {} {:.1f} {}".format(self.maGV, self.hoTen, chuyen_mon, diem, self.trangThai)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        hoTen = input()
        maXT = input()
        diemTin = float(input())
        diemCM = float(input())
        x = GiaoVien(u + 1, hoTen, maXT, diemTin, diemCM)
        arr.append(x)
    arr.sort(key = lambda x : x.tinhDiem(), reverse = True)
    for item in arr:
        print(item)
