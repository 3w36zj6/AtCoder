N = int(input())
C = list(input())
C2 = sorted(C[:])
r_n = C.count("R")

ans = 0
for i in range(r_n):
    if C[i] != C2[i]:
        ans += 1

print(ans)