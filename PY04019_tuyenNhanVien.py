cnt = 1
class ThiSinh:
    def __init__(self, tenTS, lt, th):
        self.maTS = "TS0" + str(cnt)
        self.tenTS = tenTS
        self.tongDiem = (float(lt) + float(th)) / 2
        self.trangThai = ''
        if self.tongDiem > 9.5: self.trangThai = "XUAT SAC"
        elif self.tongDiem >= 8 and self.tongDiem <= 9.5: self.trangThai = "DAT"
        elif self.tongDiem >= 5 and self.tongDiem < 8: self.trangThai = "CAN NHAC"
        else: self.trangThai = "TRUOT"
    
    def __str__(self):
        return "{} {} {:.2f} {}".format(self.maTS, self.tenTS, self.tongDiem, self.trangThai)
    
if __name__ == '__main__':
    n = int(input())
    arr = []
    for u in range(n):
        tenTS = input()
        lt = input()
        th = input()
        if float(lt) > 10: lt = lt[0] + '.' + lt[1]
        elif lt == '100': lt = '10'
        if float(th) > 10: th = th[0] + '.' + th[1]
        elif th == '100': th = '10'
        x = ThiSinh(tenTS, lt, th)
        cnt += 1
        arr.append(x)
    
    arr.sort(key = lambda x : -x.tongDiem)
    for item in arr:
        print(item)