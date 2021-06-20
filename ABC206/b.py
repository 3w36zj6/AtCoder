from decimal import Decimal
import math
N = int(input())
day = ((8*N+1)**Decimal("0.5")-1)/2
print(math.ceil(day))
