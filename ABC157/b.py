A = [list(input().split()) for i in range(3)]
N = int(input())
B = [input() for i in range(N)]

for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = ""

ans = "No"
#横
for i in range(3):
    count = 0
    for j in range(3):
        if A[i][j] == "":
            count += 1

    if count == 3:
        ans = "Yes"
        break

#縦
for j in range(3):
    count = 0
    for i in range(3):
        if A[i][j] == "":
            count += 1

    if count == 3:
        ans = "Yes"
        break

#斜め
count = 0
for i in range(3):
    if A[i][i] == "":
        count += 1

if count == 3:
    ans = "Yes"

count = 0
for i in range(3):
    if A[i][2-i] == "":
        count += 1

if count == 3:
    ans = "Yes"


print(ans)