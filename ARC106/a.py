N = int(input())


def solve():
    for a in range(1, 100):
        for b in range(1, 100):
            if pow(3, a) + pow(5, b) == N:
                return f"{a} {b}"
    return -1


print(solve())
