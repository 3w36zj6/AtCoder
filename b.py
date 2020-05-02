X = int(input())

year = 0
yen = 100
while not (yen >= X):
    #print(X)
    yen += int(yen*0.01)
    year += 1

print(year)