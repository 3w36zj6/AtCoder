S = input()
K = int(input())
print(S[K%len(S):]+S[:K%len(S)])