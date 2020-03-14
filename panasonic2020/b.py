from math import floor, ceil

H, W = map(int,input().split(" "))

if H == 1 or W == 1:
    ans = 1
elif H%2 == 0:
    ans = (H//2)*W
elif W%2 == 0:
    ans = (W//2)*H
else:
    ans = 0
    ans += floor(H/2) * floor(W/2)
    ans += ceil(H/2) * ceil(W/2)


print(int(ans))

