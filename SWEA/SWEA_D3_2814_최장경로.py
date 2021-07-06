def dfs(node, dist):
    global ans
    visited[node] = 1
    if dist > ans:
        ans = dist
    for i in graph[node]:
        if not visited[i]:
            dfs(i, dist+1)
            visited[i] = 0


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for n in range(N+1)]
    for m in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    ans = 0
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i, 1)
    print(f'#{t} {ans}')
