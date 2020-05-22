N = int(input())
A = list(map(int,input().split()))
import itertools

S = [0] + list(itertools.accumulate(A))
#print(S)
if sum(A)%N != 0:
    print(-1)
else:
    #目標
    m = sum(A)//N
    ans = 0
    for i in range(N-1):
        #print(S[i+1]-S[0],S[N]-S[i+1])
        #print((i+1)*m,N-(i+1)*m)
        if S[i+1]-S[0] != (i+1)*m:
            ans += 1

    print(ans)