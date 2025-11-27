N = int(input())
A = list(map(int, input().split()))
X = int(input())

# TLEにならないようにひとつずつ要素を見るのではなく、XをAの和で割って商を求めるとANS-1のcountが出る

# qS ≤ X < (q+1)Sになる
q = X // sum(A)

current_sum = q * sum(A)
count = q * N

# あとはXを超えるまで足し続ける
for i in range(N):
    current_sum += A[i % N]
    count += 1
    if current_sum > X:
        break

print(count)