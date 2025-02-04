n,k,q = map(int,input().split())


kl = list(map(int,input().split()))
ql = list(map(int,input().split()))

for c in ql:
    x = c-1
    if c < n and kl[x]+1 not in kl:
        kl[x] +=1
        if kl[x] > n:
            kl[x] -=1

print(" ".join(map(str,kl)))

