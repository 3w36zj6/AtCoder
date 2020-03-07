from collections import deque


S = deque(input())
Q = int(input())
QUERY = [input().split(" ") for i in range(Q)]

for query in QUERY:
    #print(query)
    if query[0] == "1":#反転
        S.reverse()
    else:#=="2"
        if query[1] == "1":
            S.appendleft(query[2])
        else:#=="2"
            S.append(query[2])
print("".join(list(S)))