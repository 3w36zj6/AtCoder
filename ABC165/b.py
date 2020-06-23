from decimal import *
from math import floor
X = int(input())

year = 0
yen = Decimal(100)
while not (yen >= X):
    #print(X)
    yen += floor(yen*Decimal("0.01"))
    year += 1

print(year)
