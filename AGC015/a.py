N, A, B = map(int,input().split())
#ans = 0
if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
else:
    if A <= B:
        print((A+B*(N-1))-(A*(N-1)+B)+1)
    else:
        print(0)