import itertools
N = int(input())
* A, = map(int, input().split())

def bit_or(L):
    ans = L[0]
    for i in L[1:]:
        ans |= i
    return ans

def bit_xor(L):
    ans = L[0]
    for i in L[1:]:
        ans ^= i
    return ans

ans = float("inf")
for bits in itertools.product([0, 1], repeat=N - 1):
    section = [A[0]]
    section_or = []
    for i, bit in enumerate(bits):
        if bit:
            section_or.append(bit_or(section))
            section = []
            section.append(A[i+1])
        else:
            section.append(A[i+1])
    section_or.append(bit_or(section))
    ans = min(bit_xor(section_or), ans)

print(ans)
