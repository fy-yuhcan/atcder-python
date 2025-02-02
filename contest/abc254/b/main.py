#aiは1から始まる
#次の数はjai-1,j-1+ai-1,j

b = []
n = int(input())    
for i in range(n):
    a = []
    #i+1のrangeでやると三角形の形になる
    for j in range(i+1):
        if j == 0 or i == j:
            a.append(1)
        else:
            c = b[i-1][j-1] + b[i-1][j]
            a.append(c)
    b.append(a)

for i in range(n):
    print(" ".join(map(str,b[i])))
        