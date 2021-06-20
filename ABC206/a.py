import math
N = int(input())

c = math.floor(1.08*N)

if c < 206:
    print("Yay!")
elif c > 206:
    print(":(")
else:
    print("so-so")
