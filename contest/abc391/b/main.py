N,M = map(int,input().split())


S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

#Tが存在するために選んだ位置からM*Mの範囲が必要
for a in range(N - M + 1):
    for b in range(N - M + 1):
        match = True
        #二つの連想配列の中で一致している時は4重ループになる
        for i in range(M):
            for j in range(M):
                if S[a+i][b+j] != T[i][j]:
                    match = False
        if match:
            print(a+1, b+1)
            exit()
        
