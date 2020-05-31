A, B = input().split()

import decimal, math
A = decimal.Decimal(A)
B = decimal.Decimal(B)

print(math.floor(A*B))