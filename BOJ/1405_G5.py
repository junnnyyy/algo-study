def dfs(r, c, np, visited, cnt):
    global not_simple
    if cnt >= move:
        return
    visited[r][c]=1 # 방문 체크
    # 순회 해보기
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 31 and 0 <= nc < 31:
            if visited[nr][nc]: # 이미 방문했던 곳이면
                not_simple += np * prob[i] # 단순하지 않은 이동
            else:
                # 단순한 이동이면 계속 가보기
                dfs(nr, nc, np*prob[i], visited, cnt+1)
                visited[nr][nc] = 0 # 단순한 이동이 결국 아니 어서 돌아왔으니 다시 방문할수 있게 방문 해제



move, e, w, s, n = map(int, input().split())
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
prob = [e/100, w/100, s/100, n/100]
visited = [[0] * 31 for _ in range(31)]

not_simple = 0
dfs(14, 14, 1, visited, 0)

print('%.10f'%(1-not_simple))