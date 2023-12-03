class Nguoi:
    def __init__(self, hoTen, sdt):
        self.__hoTen = hoTen
        self.__sdt = sdt
    
    def getTen(self):
        a = self.__hoTen.split()
        return a[len(a) - 1]
    
    def getHoDem(self):
        a = self.__hoTen.split()
        hoDem = ''
        for i in range(len(a) - 1):
            hoDem += a[i]
        return hoDem

    def __str__(self):
        return "{}: {}".format(self.__hoTen, self.__sdt)

if __name__ == '__main__':
    tu_dien = dict()
    with open("SOTAY.txt") as in_put:
        lines = in_put.readlines()
    ngay, hoten, sdt, arr = '', '', '', []
    for line in lines:
        a = line.strip().split()
        if a[0] == "Ngay":
            ngay = a[1]
        else:
            res = line.strip()
            if res.isdigit() == False:
                hoten = res
            else: sdt = res
        if len(hoten) > 0 and len(sdt) > 0:
            nguoi = Nguoi(hoten, sdt)
            hoten, sdt = '', ''
            tu_dien[nguoi] = ngay
            arr.append(nguoi)
    arr.sort(key = lambda x : (x.getTen(), x.getHoDem()))
    for item in arr:
        print(item, tu_dien[item])
    in_put.close()