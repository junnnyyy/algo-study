def bfs(dist):
    pass
    idx = 0
    r, c = dist[idx]
    Q = [r, c]
    ch = 0
    mv = 0
    piece = 0
    while Q:
        r, c = Q.pop(0)
        idx += 1
        if abs(dist[idx][0]) == abs(dist[idx][1]):
            if piece != 2:
                ch += 1
            mv += 1

        elif not dist[idx][0] or not dist[idx][1]:
            if piece != 3:
                ch += 1
            mv += 1
        else:
            if piece != 1:
                ch += 1
            mv += 1



N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
#1
kr = [-2, -1, 1, 2, 2, 1, -1, -2]
kc = [1, 2, 2, 1, -1, -2, -2, -1]
#2
br = [1, 1, -1, -1]
bc = [-1, 1, -1, 1]
#3
rr = [1, -1, 0, 0]
rc = [0, 0, 1, -1]


IDX = [tuple() for _ in range(N**2)]
for i in range(N):
    for j in range(N):
        IDX[chess[i][j]-1] = (i, j)
print(IDX)

dist = [IDX[0] for _ in range(N**2)]
for i in range(1, N**2):
    dist[i] = (IDX[i][0]-IDX[i-1][0], IDX[i][1]-IDX[i-1][1])

print(dist)
