import sys

def bfs():
    r, c = Sr, Sc
    Q = [(r, c)]
    visited[r][c] = 1
    while Q:
        r, c = Q.pop(0)
        for idx in range(4):
            nr, nc = r + dr[idx], c + dc[idx]
            if 1 <= nr < N+1 and 1 <= nc < M+1 and not visited[nr][nc]:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    return visited[Fr][Fc]-1


N, M = map(int, sys.stdin.readline().split())
grid = [[1] for _ in range(N + 1)]
grid[0].extend([1] * M)
for n in range(1, N + 1):
    grid[n].extend(list(map(int, sys.stdin.readline().split())))

H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[1] for _ in range(N + 1)]
visited[0].extend([1] * M)
for n in range(1, N + 1):
    visited[n].extend([0] * M)
# for _ in range(N+1):
#     print(visited[_])
# print()
# 시작점이 옮겨갈수 없는 부분들 미리 처리
wall = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if grid[i][j] == 1:
            wall.append((i, j))
# 벽에 위치하게 되는 경우
while wall:
    wr, wc = wall.pop()
    for i in range(wr-H+1, wr + 1):
        for j in range(wc-W+1, wc+1):
            visited[i][j] = 1
# 격자 밖으로 튀어나가게되는 경우
for i in range(N+1-H+1, N+1):
    for j in range(M+1):
        visited[i][j] = 1
for i in range(N+1):
    for j in range(M+1-W+1, M+1):
        visited[i][j] = 1
#
# for _ in range(N+1):
#     print(visited[_])

print(bfs())
