import math
n,k = map(int,input().split())
ki = list(map(int,input().split()))
a = []
for i in range(n):
    s = list(map(int,input().split()))
    a.append(s)

#あかりを持つ人の座標を取得する
bright = []
for i in range(1,n+1):
    if i in ki:
        bright.append((a[i-1]))

#あかりを持たない人の座標を取得する
v = []
for i in a:
    if i not in bright:
        v.append(i)

#全探索でそれぞれの光との距離を出して、その最小の値を求める
#それを全てのあかりを持たない人に対して行い、最大の値を求める
ans = []
for person in v:
    #最初の距離を無限大に設定
    result = float("inf")
    for i in bright:
            #あかりを持たない人のx,y座標とあかりを持つ人のx,y座標の差を出す
            dx = person[0]-i[0]
            dy = person[1]-i[1]
            #ユークリッド距離を求める
            dist = math.sqrt(dx**2+dy**2)
            result = min(result,dist)
    ans.append(result)
print(max(ans))