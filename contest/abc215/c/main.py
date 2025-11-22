s,k  = input().split()
k = int(k)

# sの文字列をリスト化
chars = list(s)
n = len(s)

res = []

# dfs
def dfs(path,used):
    if len(path) == n:
        # 文字が完成したらresに追加
        res.append("".join(path))
        return
    # ここでdfsを呼び出し
    for i in range(n):
        # すでにある場合はスキップ
        if used[i]:
            continue
        # 使用済みにする
        used[i] = True
        # 再帰的にdfsを呼び出し
        dfs(path + [chars[i]], used)
        # 使用済みを戻す
        used[i] = False

# dfs開始
dfs([], [False] * n)
uniq = sorted(set(res))

print(uniq[k-1])
