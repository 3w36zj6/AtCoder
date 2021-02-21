A, B, C = map(int, input().split())

A_end = [A % 10]

i = 0
while True:
    x = (A_end[i] * A) % 10
    if A_end[0] != x:
        A_end.append(x)
    else:
        break

    i += 1


B_C = pow(B, C, len(A_end))
print(A_end[((B_C)-1)%len(A_end)])