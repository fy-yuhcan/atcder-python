n = int(input())
Ps = list(map(int, input().split()))

P = [0, 0] + Ps 

ans = 0
x = n
while x != 1:
    x = P[x]
    ans += 1

print(ans)