s,k  = input().split()
k = int(k)

# sの文字列をリスト化
chars = sorted(s)
n = len(s)

res = []

used = [False] * n

# dfs
def dfs(path):
    if len(path) == n:
        # 文字が完成したらresに追加
        res.append("".join(path))
        return
    # ここでdfsを呼び出し
    for i in range(n):
        if used[i]:
            continue

        # iが0より大きく、かつ前の文字と同じで、かつ前の文字が使用済みでない場合はスキップ
        if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
            continue
        # 使用済みにする
        used[i] = True
        # 再帰的にdfsを呼び出し
        dfs(path + [chars[i]])
        # 使用済みを戻す
        used[i] = False

# dfs開始
dfs([])

print(res[k-1])