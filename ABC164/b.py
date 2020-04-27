from math import ceil 
A, B, C, D = map(int,input().split())

tkhs_cnt = ceil(C/B)
aok_cnt = ceil(A/D)
ans = "Yes" if aok_cnt >= tkhs_cnt else "No"
print(ans)