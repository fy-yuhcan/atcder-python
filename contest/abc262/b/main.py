n,m = map(int, input().split())
# まず全ての頂点分、falseの二次元配列を作成,頂点の番号が1始まりなのでn+1(0は捨てる)
g = [[False]*(n+1) for _ in range(n+1)]
# 各辺を入力
for _ in range(m):
    u,v = map(int, input().split())
    g[u][v] = True
    g[v][u] = True

ans = 0
# 各辺が三角形になるか
# 「a, b, c は全部違う」
# 「同じ組み合わせを 1 回だけ数えたい」
for a in range(n+1):
    for b in range(a+1,n+1):
        for c in range(b+1,n+1):
            # 三角形の条件
            if g[a][b] and g[b][c] and g[c][a]:
                ans += 1

print(ans) 