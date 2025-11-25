N = int(input())
P = list(map(int, input().split()))

Q = [0] * (N+1)

# 逆置換をする
for i in range(N):
    # P[i]番目にi+1を入れる
    v = P[i]
    # v番目にi+1を入れる
    Q[v] = i + 1


print(' '.join(map(str, Q[1:])))