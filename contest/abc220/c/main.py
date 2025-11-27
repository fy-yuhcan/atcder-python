N = int(input())
A = list(map(int, input().split()))
X = int(input())

current_sum = 0
count = 0

for i in range(1000000000):
    current_sum += A[i % N]
    count += 1
    if current_sum > X:
        break

print(count)