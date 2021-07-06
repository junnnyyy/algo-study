def move(status):
    if status == 1:
        return 0, 2
    elif status == 2:
        return 1, 3
    else:
        return 0, 3


def dfs(r, c, sr, sc, t):
    global cnt
    S = [(r, c, sr, sc, t)]

    while S:
        r0, c0, r1, c1, t = S.pop()
        if r1 == N and c1 == N:
            cnt += 1
            continue
        if r0 == r1:
            t = 1
            if c1 == N:
                continue
        elif c0 == c1:
            t = 2
            if r1 == N:
                continue
        else:
            t = 3
        s, e = move(t)
        r0, c0 = r1, c1
        for i in range(s, e):
            nr, nc = r1 + dr[i], c1 + dc[i]
            if 0 <= nr <= N and 0 <= nc <= N:
                if (i == 0 or i == 2) and not home[nr][nc]:
                    S.append((r0, c0, nr, nc, t))
                elif i == 1 and not home[nr][nc] and not home[nr][c1] and not home[r1][nc]:
                    S.append((r0, c0, nr, nc, t))


N = int(input())
home = [[1]+list(map(int, input().split())) for _ in range(N)]
home = [[1 for _ in range(N+1)]] + home
dr, dc = [0, 1, 1], [1, 1, 0]
cnt = 0
dfs(1, 1, 1, 2, 1)
print(cnt)
