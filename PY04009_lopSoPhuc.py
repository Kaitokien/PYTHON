
class SoPhuc:
    def __init__(self, thuc, ao):
        self.__ao = ao
        self.__thuc = thuc

    def __add__(self, other):
        tong_thuc = self.__thuc + other.__thuc
        tong_ao = self.__ao + other.__ao
        return SoPhuc(tong_thuc, tong_ao)
    
    def __mul__(self, other):
        tich_thuc = self.__thuc * other.__thuc + self.__ao * other.__ao * -1
        tich_ao = self.__thuc * other.__ao + self.__ao * other.__thuc
        return SoPhuc(tich_thuc, tich_ao)
    
    def __str__(self):
        real = self.__thuc
        fake = self.__ao
        if self.__ao > 0:
            return f'{real} + {fake}i'
        else:
            return f'{real} - {fake}i'

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        a = [int(i) for i in input().split()]
        u = SoPhuc(a[0], a[1])
        v = SoPhuc(a[2], a[3])
        c = (u + v) * u
        d = (u + v) * (u + v)
        print(c, d, sep = ', ')
