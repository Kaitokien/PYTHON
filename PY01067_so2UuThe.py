def check(s):
    return s.count("2") * 2 >= len(s) + 1

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        a, dem = ["1", "2"], 0
        n = int(input())
        while dem < n:
            s = a[0]
            if check(s):
                print(s, end = ' ')
                dem += 1
            a.append(s + "0")
            a.append(s + "1")
            a.append(s + "2")
            del a[0]
        print()