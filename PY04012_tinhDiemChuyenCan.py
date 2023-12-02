from math import *

class SinhVien:
    def __init__(self, maSV, hoTen, lop):
        self.maSV = maSV
        self.hoTen = hoTen
        self.lop = lop
        self.diem = 10
        self.trangThai = ''
    
    def getMa(self):
        return self.maSV

    def setDiem(self, diemDanh):
        for item in diemDanh:
            if item == 'm': self.diem -= 1
            elif item == 'v': self.diem -= 2
        if self.diem <= 0:
            self.diem = 0
            self.trangThai = "KDDK"
    
    def __str__(self):
        return "{} {} {} {} {}".format(self.maSV, self.hoTen, self.lop, self.diem, self.trangThai)

if __name__ == '__main__':
    n = int(input())
    arr = []
    tu_dien = dict()
    for u in range(n):
        maSV = input()
        tenSV = input()
        lop = input()
        x = SinhVien(maSV, tenSV, lop)
        tu_dien[maSV] = x
        arr.append(x)
    for _ in range(n):
        a = input().split()
        tu_dien[a[0]].setDiem(a[1])
    for item in arr:
        print(item)
