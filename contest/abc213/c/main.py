import bisect

h,w,n = map(int, input().split())
x = []
y = []
for _ in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

rows = sorted((set(x)))
columns = sorted((set(y)))

for i in range(n):
    compressed_x = bisect.bisect_left(rows, x[i]) + 1
    compressed_y = bisect.bisect_left(columns, y[i]) + 1
    print(compressed_x, compressed_y)




