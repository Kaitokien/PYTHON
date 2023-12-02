class ThiSinh:
    def __init__(self, ten, dob, m1, m2, m3):
        self.__ten = ten
        self.__dob = dob
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        
    def __str__(self):
        return f'{self.__ten} {self.__dob} {(self.__m1 + self.__m2 + self.__m3):.1f}'

if __name__ == '__main__':
    name = input()
    dob = input()
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    s = ThiSinh(name, dob, m1, m2, m3)
    print(s)