from math import *

n = input()
if len(n) == 1:
    print(1)
else:
    dem = 0
    while len(n) > 1:
        n = str(sum(ord(x) - ord("0") for x in n))
        dem += 1
    print(dem)