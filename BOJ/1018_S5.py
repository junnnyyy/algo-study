def counting(sr, sc):
    val = 0
    start = board[sr][sc]
    for i in range(0, 8):
        nr = sr + i
        for j in range(0, 8):
            nc = sc + j
            if not nr % 2:
                if not nc % 2 and board[nr][nc] != start:
                    val += 1
                elif nc % 2 and board[nr][nc] == start:
                    val += 1
            else:
                if not nc % 2 and board[nr][nc] == start:
                    val += 1
                elif nc % 2 and board[nr][nc] != start:
                    val += 1
    return val

N, M = map(int, input().split())
board = [input() for _ in range(N)]
print(board)
res = N * M # 갱신해 나갈값
# 시작점 바꿔가면서 카운팅
for r in range(0, N-7):
    for c in range(0, M-7):
        cnt = counting(r, c)
    if cnt > 32:
        cnt = 64 - cnt
    res = cnt
print(res)