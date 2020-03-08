

N_A, N_B, N_M = map(int,input().split(" "))
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
M = [list(map(int,input().split(" "))) for i in range(N_M)]

candidates = [min(A)+min(B),]

for m in M:
    #print(A[m[0]-1] + B[m[1]-1] - m[2])
    candidates.append(A[m[0]-1] + B[m[1]-1] - m[2])

print(min(candidates))