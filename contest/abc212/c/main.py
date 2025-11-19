n,m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

if A[0] > B[0]:
    ans = A[0] - B[0]
else:
    ans = B[0] - A[0]

i = j = 0

while i < n and j < m:
    ans = min(ans, abs(A[i] - B[j]))
    if A[i] < B[j]:
        i += 1
    elif A[i] > B[j]:
        j += 1
    else:
        ans = 0
        break
print(ans)