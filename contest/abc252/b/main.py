n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

m = max(a)

ok = False

for i in range(k): 
    if a[b[i]-1] == m:
        ok = True

if ok:
    print("Yes")
else:  
    print("No")