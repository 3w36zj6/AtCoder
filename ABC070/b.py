A, B, C, D = map(int,input().split())
alice = set(range(A, B+1))
bob = set(range(C, D+1))
print(max(len(alice & bob)-1,0))