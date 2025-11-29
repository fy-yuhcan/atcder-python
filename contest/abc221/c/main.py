N = input().strip()

digits = sorted(N, reverse=True)
d = len(digits)

ans = 0

# ビット全探索で分割、rangeは1から(1<<d)-1まで
for mask in range(1, (1 << d) - 1):
    a_digits = []
    b_digits = []

    for i in range(d):
        # iの数まで右シフトして、ビットが立っているかどうかで振り分け
        if (mask >> i) & 1:
            a_digits.append(digits[i])
        else:
            b_digits.append(digits[i])

    A = int(''.join(a_digits))
    B = int(''.join(b_digits))

    if A == 0 or B == 0:
        continue

    ans = max(ans, A * B)

print(ans)