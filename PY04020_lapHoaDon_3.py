from math import *

class MatHang:
    def __init__(self, maHang, tenHang, soLuong, donGia, tienChietKhau):
        self.maHang = maHang
        self.tenHang = tenHang
        self.soLuong = soLuong
        self.donGia = donGia
        self.tienChietKhau = tienChietKhau
    
    def tinhTien(self):
        return self.donGia * self.soLuong - self.tienChietKhau
    
    def __str__(self):
        tongTien = self.donGia * self.soLuong - self.tienChietKhau
        return "{} {} {} {} {} {}".format(self.maHang, self.tenHang, self.soLuong, self.donGia, self.tienChietKhau, tongTien)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        maHang = input()
        tenHang = input()
        soLuong = int(input())
        donGia = int(input())
        tienChietKhau = int(input())
        x = MatHang(maHang, tenHang, soLuong, donGia, tienChietKhau)
        arr.append(x)
    arr.sort(key = lambda x : x.tinhTien(), reverse = True)
    for item in arr:
        print(item)
