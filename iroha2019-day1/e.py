N, A, B = map(int,input().split())
D = list(map(int,input().split()))
D.sort()
D = [0] + D + [N+1]

tmp = 0
ans = 0
for d in D:
    ans += (d - tmp - 1) - (d - tmp - 1)//A

    
    tmp = d

print(ans)

#PPDDPPDPPP

