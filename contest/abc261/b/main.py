# 総当たりn行n列
n = int(input())
a = [input() for _ in range(n)]
# 判定ふらぐ
ok = True
for i in range(n):
    for j in range(n):
        # 同じ時はむし
        if i == j:
            continue
        # 判定
        if a[i][j] == 'W' and a[j][i] != 'L':
            ok = False
        if a[i][j] == 'L' and a[j][i] != 'W':
            ok = False
        if a[i][j] == 'D' and a[j][i] != 'D':
            ok = False
        
        # 違ったらbreak
        if not ok:
            break
    if not ok:
        break

print("correct" if ok else "incorrect")


