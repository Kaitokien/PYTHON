from datetime import datetime

class Khach:
    def __init__(self, ma, hoTen, phong, ngayNhan, ngayTra, phatsinh):
        self.ma = "KH" + '{:02d}'.format(ma)
        self.hoten = hoTen.strip()
        self.phong = phong.strip()
        bd = datetime.strptime(ngayNhan.strip(), "%d/%m/%Y")
        kt = datetime.strptime(ngayTra.strip(), "%d/%m/%Y")
        self.ngay = (kt - bd).days + 1
        self.bonus = phatsinh

    def tinhTien(self):
        if self.phong[0] == '1': return 25 * self.ngay + self.bonus
        elif self.phong[0] == '2': return 34 * self.ngay + self.bonus
        elif self.phong[0] == '3': return 50 * self.ngay + self.bonus
        else: return 80 * self.ngay + self.bonus
    
    def __str__(self):
        thanhtien = self.tinhTien()
        return '{} {} {} {} {}'.format(self.ma, self.hoten, self.phong, self.ngay, thanhtien)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        hoTen = input()
        phong = input()
        ngayNhan = input()
        ngayTra = input()
        phatsinh = int(input().strip())
        x = Khach(u + 1, hoTen, phong, ngayNhan, ngayTra, phatsinh)
        arr.append(x)
    arr.sort(key = lambda x : x.tinhTien(), reverse = True)
    for item in arr:
        print(item)
