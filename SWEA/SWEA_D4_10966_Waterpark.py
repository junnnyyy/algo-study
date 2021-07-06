def bfs(wr, wc):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = [0] * (N*M)
    front, rear = 0, 0
    Q[front] = (wr, wc)
    rear += 1
    while front < rear:
        r, c = Q[front]
        front += 1
        dist = visited[r][c]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] > dist + 1:
                Q[rear] = (nr, nc)
                rear += 1
                visited[nr][nc] = dist + 1


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    maps = [input() for n in range(N)]
    visited = [[0 if maps[i][j] == 'W' else 1000000 for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                bfs(i, j)
    total = sum(sum(visited[_]) for _ in range(N))
    print('#{} {}'.format(t, total))