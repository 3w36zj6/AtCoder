A, B, W = map(int, input().split())

ans_min = 0
ans_max = 0

for i in range(W * 1000 // B, 0, -1):
    if i == (W * 1000 // B):
        if W * 1000 - i * B == 0:
            ans_min = (W * 1000 // B)
            break
    else:
        if A <= ((W * 1000 - i * B) / ((W * 1000 // B) - i + 1)) <= B:
            ans_min = (W * 1000 // B) + 1
            break

for i in range(W * 1000 // A, 0, -1):
    if i == (W * 1000 // A):
        if W * 1000 - i * A == 0:
            ans_max = (W * 1000 // A)
            break
    else:
        if A <= ((W * 1000 - i * A) / ((W * 1000 // A) - i)) <= B:
            ans_max = (W * 1000 // A)
            break

if ans_min == 0 or ans_max == 0:
    print("UNSATISFIABLE")
else:
    print(ans_min, ans_max)
