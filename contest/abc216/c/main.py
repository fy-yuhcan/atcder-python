# C - Many Balls
# Aはこの中にボールを1つ増やす
# bはボールを2倍
# 120回以内で箱の中をN個にする
# N <= 10^18
N = int(input())

ans = []
x = N
while x > 0:
    if x % 2 == 1:
        ans.append('A')
        x -= 1
    else:
        ans.append('B')
        x //= 2

ans.reverse()
print(''.join(ans))

