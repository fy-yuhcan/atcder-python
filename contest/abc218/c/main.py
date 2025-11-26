#  ABC 218 C - Shapes
# 二次元グリッドST,STが90度回転、平行移動の繰り返しで一致するか
# N <= 200
# S,T は # と . のみからなる
# S,T は 1 つ以上 # を含む

# 左上を固定して合うようにずらす、左上に来るように合わす
# 左上のラインを合わせてそれを標準形にして合うかどうかをみる

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

# #があるセルの座標のみを記録する
def get_cells(grid):
    cells = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                cells.append((i, j))
    return cells

s_cells = get_cells(S)
t_cells = get_cells(T)

# #の数が違ったら無理
if len(s_cells) != len(t_cells):
    print("No")
    exit()

# 正規化：左上を(0,0)に持ってくる
def normalize(cells):
    min_i = min(i for i, j in cells)
    min_j = min(j for i, j in cells)
    normalized = sorted((i - min_i, j - min_j) for i, j in cells)
    return normalized

target = normalize(t_cells)

# 90度回転(N-1-iはjの変換)
def rotate(cells):
    return [(j, N - 1 - i) for i, j in cells]

current = s_cells

# 4回回転させてみて、正規化して一致するか確認
for _ in range(4):
    normalized = normalize(current)
    if normalized == target:
        print("Yes")
        exit()
    current = rotate(current)
print("No")
