A, B, N = map(int,input().split())

if B == 1:
    ans = 0
elif B == N:
    ans = A - 1
elif B < N:
    ans = A - 1
else:#B > N
    ans = int(N*A/B)-A*int(N/B)
    #print(int(N*A/B)-A*int(N/B))

print(ans)