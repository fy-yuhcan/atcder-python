# 盤面シミュレーションは制約的に無理（H,W ≤ 10^9）

# 削除後の行・列番号は、「爆弾のある行・列をソートして順位を見るだけ」

# だからやることは：

# A,B を配列に保存

# sorted(set(A)), sorted(set(B))

# 二部探索で で「元の行/列 → 圧縮後の番号」を作る

# 元の順で出力


import bisect

h,w,n = map(int, input().split())
x = []
y = []
for _ in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

# 座標圧縮するために、重複を排除してソートしたリストを作成
rows = sorted((set(x)))
columns = sorted((set(y)))

for i in range(n):
    # 座標圧縮、何番目の要素となるか調べる
    compressed_x = bisect.bisect_left(rows, x[i]) + 1
    compressed_y = bisect.bisect_left(columns, y[i]) + 1
    print(compressed_x, compressed_y)




