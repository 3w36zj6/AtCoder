import math
from decimal import Decimal
R, X, Y = map(int, input().split())

d2 = X ** 2 + Y ** 2
d = Decimal(d2) ** Decimal("0.5")

if d2 < R ** 2:
    print(2)
elif d % R == 0:
    print(d // Decimal(R))
else:
    print(d // Decimal(R) + Decimal(1))
