def recursive_dfs(v, adj):
    d_s.append(v)
    top = d_s.pop()
    if not d_visited[top]:
        d_visited[top] = 1
        d_path.append(top)
        for i in range(len(adj)):
            if adj[top][i] == 1 and not d_visited[i]:
                return recursive_dfs(i, adj)
        if not d_s:
            return
##틀림

# def dfs(v, adj):
#     # 방문여부 체크
#     visited = [0] * len(adj)
#     # 리턴할 경로
#     path = []
#     # 돌아갈곳 담을 Stack
#     S = [v]
#     # v 부터 시작
#     while S:
#         top = S.pop()
#         if not visited[top]:
#             visited[top] = 1
#             path.append(top)
#             # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
#             for i in range(len(adj) - 1, 0, -1):
#                 if adj[top][i] == 1 and not visited[i]:
#                     S.append(i)
#     return path


def bfs(v, adj):
    visited = [0] * len(adj)
    path = []
    Q = [v]
    visited[v] = 1
    while Q:
        top = Q.pop(0)
        path.append(top)
        for i in range(len(adj)):
            if adj[top][i] == 1 and not visited[i]:
                visited[i] = 1
                Q.append(i)
    return path


N, M, V = map(int, input().split())
adj = [[0] * (N + 1) for n in range(N + 1)]
for m in range(M):
    x, y = map(int, input().split())
    adj[x][y], adj[y][x] = 1, 1

d_path = []
d_visited = [0]*len(adj)
d_s = []

recursive_dfs(V, adj)
print(*d_path)
print(*bfs(V, adj))
