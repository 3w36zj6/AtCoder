N, X = map(int, input().split())
A = list(map(int, input().split()))
A_ = list(filter(lambda a: a != X, A))
if A_:
    print(*A_)
