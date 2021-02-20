S = input()
ans = "Yes"
for i, s in enumerate(S):
    if i % 2 == 0 and s.isupper():
        ans = "No"
        break
    if i % 2 == 1 and s.islower():
        ans = "No"
        break

print(ans)