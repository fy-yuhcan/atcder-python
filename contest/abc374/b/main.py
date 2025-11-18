s = input()
t = input()

# どちらか大きい方を撮ることで比較できるようにする
n = max(len(s),len(t))

if s== t:
    print(0)
    exit()

for i in range(n):
    # nでなくiで比較する理由は、文字列の長さが違う場合に対応するため
    if i >= len(s) or i >= len(t):
        print(i+1)
        exit()
    if s[i] != t[i]:
        print(i + 1)
        exit()
