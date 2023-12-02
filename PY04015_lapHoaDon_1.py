from math import *
cnt = 1
class KhachHang:
    def __init__(self, ma, hoTen, cu, moi):
        self.ma = "KH" + "{:02d}".format(ma)
        self.hoTen = hoTen
        self.tongTien = 0
        chiSo = moi - cu
        if chiSo <= 50: 
            self.tongTien = 100 * chiSo + (100 * chiSo) / 50
        elif chiSo <= 100:
            self.tongTien = (50 * 100 + (chiSo - 50) * 150) *  1.03
        else:
            self.tongTien = (50 * 100 + 50 * 150 + (chiSo - 100) * 200) * 1.05

    def __str__(self):
        return "{} {} {}".format(self.ma, self.hoTen, round(self.tongTien))
    
if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        hoTen = input()
        cu = int(input())
        moi = int(input())
        x = KhachHang(u + 1, hoTen, cu, moi)
        cnt += 1
        arr.append(x)
    
    arr.sort(key = lambda x : -x.tongTien)
    for item in arr:
        print(item)