X = int(input())
for i in range(1,9):
    if X >= 400+200*(8-i):
        print(i)
        break