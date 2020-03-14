from decimal import *
getcontext().prec = 230

from math import sqrt
a, b, c = map(Decimal,input().split(" "))

if a + b - c + 2 * (a*b).sqrt() < 0 :
    ans = "Yes"
else:
    ans = "No"
print(ans)
