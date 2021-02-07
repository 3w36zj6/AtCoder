from collections import deque

N, M = map(int, input().split())
road = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    road[A].append(B)
    road[B].append(A)

todo = deque([1])  # 探索スタート地点
visited = [False] * (N+1)  # 探索済みリスト
visited[1] = True

answers = [0] * (N+1)  # 道しるべ

# 幅優先探索
while todo:
    now = todo.popleft()  # 次の探索地点を1つ取り出す
    for new in road[now]:  # 次に行こうと思えば行けるポイント
        if visited[new]:  # 探索済み
            continue
        visited[new] = True  # 訪れてなかったら訪れたことにする
        answers[new] = now  # newの前の地点を代入
        todo.append(new)  # newが次の現在地の候補となる


print("Yes")
for answer in answers[2:]:
    print(answer)

'''
探索候補に探索スタート地点を格納
while 探索候補が空っぽになるまで
    探索候補から次の探索地点を1つ取り出す pop popleft
    探索済みリストに取り出した地点を格納 ここが現在地点
    for 地点 in 次に行こうと思えば行けるポイント
        if その地点は既に探索済み？
            continue
        if その地点は既に探索候補にある？ 閉路があるなら可能性あり 木なら可能性なし
            continue
        探索候補に追加
'''