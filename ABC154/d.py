
N, K = map(int,input().split(" "))
P = map(int,input().split(" "))

E = []
for p in P:
    e = 0
    for i in range(1,p+1):
        e += i/p
    E.append(e)



#print(E)
ANS = s = sum(E[0:K])


for i in range(1,N-K+1):
    #sum(E[i:i+K])
    s = s+E[i+K-1]-E[i-1]
    #print(ANS, s)
    ANS = max(ANS, s)


print(ANS)




