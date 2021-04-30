from collections import deque

H, W = map(int, input().split())
C = [input() for i in range(H)]
road = [[[] for i in range(W)] for i in range(H)]

for w in range(W):
    for h in range(H):
        # C[h][w]
        if C[h][w] == "s":
            start_h, start_w = h, w

        if h > 0 and C[h-1][w] != "#":
            road[h][w].append([h-1, w])
        if h < H-1 and C[h+1][w] != "#":
            road[h][w].append([h+1, w])
        if w > 0 and C[h][w-1] != "#":
            road[h][w].append([h, w-1])
        if w < W-1 and C[h][w+1] != "#":
            road[h][w].append([h, w+1])

todo = deque([[start_h, start_w]])  # 探索スタート地点
visited = [[False for i in range(W)] for i in range(H)]  # 探索済みリスト

visited[start_h][start_w] = True

ans = "No"

# 深さ優先探索
while todo:
    now_h, now_w = todo.pop()  # 次の探索地点を1つ取り出す
    for new_h, new_w in road[now_h][now_w]:  # 次に行こうと思えば行けるポイント
        if visited[new_h][new_w]:  # 探索済み
            continue
        visited[new_h][new_w] = True  # 訪れてなかったら訪れたことにする
        if C[new_h][new_w] == "g":
            ans = "Yes"
            break
        todo.append([new_h, new_w])  # newが次の現在地の候補となる

print(ans)


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
