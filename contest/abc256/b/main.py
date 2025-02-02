n = int(input())

a = list(map(int,input().split()))
result = 0
#ここで初期の状態を作って、バッターが出たらその状態を表す
current = [0,0,0,0]
for x in a:
    #次の状態を作る
    next = [0,0,0,0]
    #最初のコマは1
    current[0] = 1
    for i in range(4):
        #もしi番目に人がいて、もし現在地+xが4以上なら、結果に1を足す
        if current[i] == 1:
            if i +x >=4:
                result += 1
            else:
                next[i+x] = 1
    current = next
print(result)