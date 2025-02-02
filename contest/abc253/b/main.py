h,w = map(int,input().split())

current = []
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == "o":
            current.append((i,j))

x = abs(current[0][0] - current[1][0])
y = abs(current[0][1] - current[1][1])


result = x+y
print(result)