A, B, C = map(int,input().split())
K = int(input())

cnt = 0
ans = "No"
while cnt <= K:
    if not A < B:
        B *= 2
        cnt += 1
        continue
    if not B < C:
        C *= 2
        cnt += 1
        continue
    if A < B < C:
        ans = "Yes"
        break


print(ans)