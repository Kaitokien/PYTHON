t = int(input())
while t > 0:
    s = ''
    d, m = map(int, input().split())
    if m == 1:
        if d >= 20: s = 'Bao Binh'
        else: s = 'Ma Ket'
    elif m == 2:
        if d >= 19: s = 'Song Ngu'
        else: s = 'Bao Binh'
    elif m == 3:
        if d >= 21: s = 'Bach Duong'
        else: s = 'Song Ngu'
    elif m == 4:
        if d >= 20: s = 'Kim Nguu'
        else: s = 'Bach Duong'
    elif m == 5:
        if d >= 21: s = 'Song Tu'
        else: s = 'Kim Nguu'
    elif m == 6:
        if d >= 21: s = 'Cu Giai'
        else: s = 'Song Tu'
    elif m == 7:
        if d >= 23: s = 'Su Tu'
        else: s = 'Cu Giai'
    elif m == 8:
        if d >= 23: s = 'Xu Nu'
        else: s = 'Su Tu'
    elif m == 9:
        if d >= 23: s = 'Thien Binh'
        else: s = 'Xu Nu'
    elif m == 10:
        if d >= 23: s = 'Thien Yet'
        else: s = 'Thien Binh'
    elif m == 11:
        if d >= 23: s = 'Nhan Ma'
        else: s = 'Thien Yet'
    elif m == 12:
        if d >= 22: s = 'Ma Ket'
        else: s = 'Nhan Ma'
    print(s)
    t -= 1