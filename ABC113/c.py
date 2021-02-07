N, M = map(int, input().split())
cities = [list(map(int, input().split())) for i in range(M)]

prefectures = [[] for i in range(N+1)]

for i, city in enumerate(cities):
    p = city[0]
    y = city[1]
    prefectures[p].append({"year": y, "city": i+1})

for i in range(N+1):
    prefectures[i] = list(sorted(prefectures[i], key=lambda x: x["year"]))

answers = [""] * (M+1)

for p, prefecture in enumerate(prefectures):
    for i, city in enumerate(prefecture):
        answers[city["city"]] = str(p).zfill(6)+str(i+1).zfill(6)


for answer in answers[1:]:
    print(answer)
