N, X, Y = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
#print(A)
X_cnt = Y_cnt = 0
while len(A) > 0:
    #takahashi
    if X_cnt < N//2:
        X_cnt += 1
        X += A.pop(0)

    if len(A) == 0:
        break

    #aoki
    if Y_cnt < N//2:
        Y_cnt += 1
        Y += A.pop(0)

if X == Y:
    ans = "Draw"
elif X > Y:
    ans = "Takahashi"
else:
    ans = "Aoki"
print(ans)