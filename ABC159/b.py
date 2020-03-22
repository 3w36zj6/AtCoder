S = input()
N = len(S)

def is_kaibun(str_):
    return str_ == str_[::-1]

if is_kaibun(S) and is_kaibun(S[:(N-1)//2]) and is_kaibun(S[(N+3)//2-1:]):
    print("Yes")
else:
    print("No")