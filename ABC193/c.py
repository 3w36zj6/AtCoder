N = int(input())

from math import ceil, log, sqrt

checked = set()
count = 0


for a in range(2, ceil(sqrt(N))+1):
    for b in range(2, ceil(log(N, a))+1):
        a_b = a ** b
        if a_b > N:
            continue
        if not a_b in checked:
            checked.add(a_b)
            count += 1

print(N - count)
