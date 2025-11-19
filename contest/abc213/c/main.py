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




