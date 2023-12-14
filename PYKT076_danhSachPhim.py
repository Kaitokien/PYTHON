tu_dien = dict()
class Phim:
    def __init__(self, maPhim, theloai, ngaychieu, tenphim, sotap):
        self.maPhim = 'P{:03d}'.format(maPhim)
        self.theloai = theloai
        self.ngaychieu = ngaychieu
        self.tenphim = tenphim
        self.sotap = sotap
        res = self.ngaychieu.split('/')
        self.date = res[2] + res[1] + res[0]
     
    def __str__(self):
        return "{} {} {} {} {}".format(self.maPhim, self.theloai, self.ngaychieu, self.tenphim, self.sotap)

if __name__ == "__main__":
    arr = []
    n, m = map(int, input().split())
    for i in range(n):
        theloai = input()
        ma = 'TL{:03d}'.format(i + 1)
        tu_dien[ma] = theloai
    for i in range(m):
        ma, ngaychieu, tenphim, sotap = input(), input(), input(), int(input())
        phim = Phim(i + 1, tu_dien[ma], ngaychieu, tenphim, sotap)
        arr.append(phim)
    arr.sort(key = lambda x : (x.date, x.tenphim, -x.sotap))
    for item in arr:
        print(item)