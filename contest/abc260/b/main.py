# まず数学の上からx人、次に残りから英語のy人、残りから数学と英語の合計からz人、残りは不合格
# 同じの時は番号が小さいほう
# 合格になった受験生の番号を小さい順に改行区切りで出力sうる
n,x,y,z = map(int,input().split())
math = list(map(int,input().split()))
eng = list(map(int,input().split()))

a = []
for i in range(n):
    # 何番目の受験生かを持つようにする
    a.append((i,math[i],eng[i]))

# 順番なしの重複なしの集合
passed = set()

# key=lamda　x:(-x[1],x[0]) で数学の点数が高い順、同じなら番号が小さい順にソート
mathpassed = sorted(a,key=lambda x:(-x[1],x[0]))
for i in range(x):
    # 合格者の番号をセットに追加
    passed.add(mathpassed[i][0])

remain = [s for s in a if s[0] not in passed]
engpassed = sorted(remain,key=lambda x:(-x[2],x[0]))
for i in range(y):
    passed.add(engpassed[i][0])

remain = [s for s in a if s[0] not in passed]
totalpassed = sorted(remain,key=lambda x:(-(x[1]+x[2]),x[0]))
for i in range(z):
    passed.add(totalpassed[i][0])

ans = sorted(passed)
for i in ans:
    print(i+1)

