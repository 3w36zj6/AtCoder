N = int(input())
prizes = set()

for prize in [input() for i in range(N)]:
    prizes.add(prize)

print(len(prizes))