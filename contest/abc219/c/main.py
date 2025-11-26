# ABC219 C - neo-lexicographic Ordering
# sのソートを辞書順にするが、xを基準にしてソートする
x = input()
n = int(input())
s = [input() for _ in range(n)]

ans = []

# xの対応表を作成する
def create_mapping(x):
    mapping = {}
    for i, c in enumerate(x):
        mapping[c] = chr(ord('a') + i)
    return mapping

# ここで辞書型が返ってくる{a: 'b'...}
mapping =create_mapping(x)

# word = 'ba', mapping = {'a': 'b'...}
def conversion(word,mapping):
    new_s = ''
    # 'ba' -> 'ab'
    for c in word:
        # mappingのkeyに対応するvalueをsとする
        new_s += mapping[c]
    return new_s

for i in range(n):
    new_s = conversion(s[i],mapping)
    # (new_s, originalのs)のタプルをansに追加
    ans.append((new_s,s[i]))
# new_sでソートして、originalのsを出力
ans.sort()
for _, original in ans:
    print(original)