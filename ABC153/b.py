H, A = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)

ans = "No"
for a in A:
    H -= a
    if H <= 0:
        ans = "Yes"
        break

print(ans)