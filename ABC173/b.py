N = int(input())
a = w = t = r = 0
for i in range(N):
    s = input()
    if s == "AC":
        a += 1
    elif s == "WA":
        w += 1
    elif s == "TLE":
        t += 1
    elif s == "RE":
        r += 1

print("AC x {}".format(a))
print("WA x {}".format(w))
print("TLE x {}".format(t))
print("RE x {}".format(r))