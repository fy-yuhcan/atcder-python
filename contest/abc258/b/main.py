n = int(input())

mp = [list(map(int,input().split())) for i in range(n)]

start = (0,0)
for i in range(n):
    for j in range(len(mp[i])):
        if mp[i][j] > mp[start[0]][start[1]]:
            start = (i,j)
ans = []
print(mp[1][0])

print(star)
for i in range(n-1):
    for j in range(len(mp[i])):
        if start[0]+1 < n and start[0]-1 >= 0:
            if max(mp[start[0]+1]) > max(mp[start[0]-1]):
                start = (i+start[0],j+start[1])
                ans.append(mp[start[0]][start[1]])
            else:
                start = (start[0]-i,start[1]-j)
                ans.append(mp[start[0]][start[1]])
        else:
            if max(mp[start[0]-1]) > max(mp[start[0]-n]):
                ans.append(max(mp[start[0]-1]))
                start = (start[0]-i,start[1]-j)
            else:
                ans.append(max(mp[start[0]-n]))
                start = (0,start[j])

print(ans)

