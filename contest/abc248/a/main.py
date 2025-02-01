s = input()
si = int(s)

seq = set()
for i in range(10):
    seq.add(str(i))

for i in range(len(s)):
    if s[i] in seq:
        seq.remove(s[i])

print("".join(seq))