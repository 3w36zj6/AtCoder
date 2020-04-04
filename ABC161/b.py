N, M = map(int,input().split(" "))
A = list(map(int,input().split(" ")))
A_sum = sum(A)

A.sort(reverse=True)
cnt = 0
for a in A:
    if a >= A_sum/(4*M):
        cnt += 1
    else:
        ans = "No"

    if cnt == M:
        ans = "Yes"
        break

print(ans)