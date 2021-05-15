import itertools
S = input()

includes = []
unknowns = []

for i in range(10):
    if S[i] == "o":
        includes.append(str(i))
    elif S[i] == "?":
        unknowns.append(str(i))

if len(includes) > 4:
    print(0)
elif len(includes) == 4:
    print(24)
else:
    passwords = set()
    for perm in itertools.permutations(includes+["?", ]*(4-len(includes)), 4):
        for replaces in itertools.product(includes+unknowns, repeat=perm.count("?")):
            password = "".join(perm)
            for r in replaces:
                password = password.replace("?", r, 1)
            passwords.add(password)

    print(len(passwords))
