from math import floor, ceil

A, B = map(int,input().split(" "))

#print(A/0.08,B/0.10)

candidates = [floor(A/0.08),ceil(A/0.08),floor(B/0.10),ceil(B/0.10)]

#print(candidates)

ans = -1
for candidate in candidates:
    #print(candidate*0.08,candidate*0.10)
    if floor(candidate*0.08) == A and floor(candidate*0.10) == B:
        ans = candidate
        break
print(ans)