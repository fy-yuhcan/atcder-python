n = int(input())

s = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = t[:]

# 2周させることで全てチェックする
for i in range(2 * n):
    # 現在地と次の地点
    cur = i % n
    nxt = (cur + 1) % n

    # 次のノードの重み+現在の重み
    cand = ans[cur] + s[cur]

    # 答えをcandと比較して小さい方を採用
    ans[nxt] = min(ans[nxt], cand)

for a in ans:
    print(a)