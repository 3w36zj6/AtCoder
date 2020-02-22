N, K = map(int,input().split())

def f_10_to_n(X, n):
    X_dumy = X
    ans = ''
    while X_dumy>0:
        ans = str(X_dumy%n)+ans
        X_dumy = int(X_dumy/n)
    return ans

print(len(f_10_to_n(N, K)))