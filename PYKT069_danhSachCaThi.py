class CaThi:
    def __init__(self, maCa, ngayThi, gioThi, phongThi):
        self.__maCa = "C{:03d}".format(maCa)
        self.__ngayThi = ngayThi
        self.__gioThi = gioThi
        self.__phongThi = phongThi

    def getNgayThi(self):
        return self.__ngayThi

    def getMaCa(self):
        return self.__maCa
    
    def getGioThi(self):
        return self.__gioThi

    def __str__(self):
        return "{} {} {} {}".format(self.__maCa, self.__ngayThi, self.__gioThi, self.__phongThi)
    
if __name__ == '__main__':
    with open("CATHI.in") as in_put:
        line = in_put.read()
    arr, ans = line.split(), []
    t, idx = int(arr[0]), 1
    for u in range(t):
        ngayThi = arr[idx]
        idx += 1
        gioThi = arr[idx]
        idx += 1
        phongThi = arr[idx]
        idx += 1
        cathi = CaThi(u + 1, ngayThi, gioThi, phongThi)
        ans.append(cathi)
    ans.sort(key = lambda x : (x.getNgayThi(), x.getGioThi(), x.getMaCa()))
    for item in ans:
        print(item)