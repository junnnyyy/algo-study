dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, color):
    global tmp_ans, is_bomb
    q = [(r, c)]
    candi = []
    checked[r][c] = 1
    while q:
        r, c = q.pop(0)
        candi.append((r, c))
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 6 and 0 <= nc < 12 and not checked[nr][nc] and lst[nr][nc] == color:
                q.append((nr, nc))
                checked[nr][nc] = 1
    if len(candi) >= 4:
        is_bomb = True
        print(candi)
        for i in range(len(candi)):
            xr, xc = candi[i]
            lst[xr][xc] = 0

def rm_zero(lst):
    for i in range(6):
        y = len(lst[i])
        for j in range(y-1, -1, -1):
            if lst[i][j] == 0:
                lst[i].pop(j)
    return

def padding(lst):
    for i in range(6):
        y = len(lst[i])
        val = 12-y
        lst[i] += ['.'] * val

lst = [[0] * 12 for _ in range(6)]
for i in range(12):
    tmp = list(input())
    for j in range(len(tmp)):
        lst[j][11-i] = tmp[j]

ans = 0
is_bomb = True
while True:
    checked = [[0] * 12 for _ in range(6)]
    is_bomb = False
    for i in range(6):
        tmp_ans = 0
        y = len(lst[i])
        for j in range(y):
            if lst[i][j] != '.':
                print(i, j, lst[i][j])
                bfs(i, j, lst[i][j])
    rm_zero(lst)
    padding(lst)
    if is_bomb:
        print(ans)
        ans += 1
    else:
        break
    for _ in range(6):
        print(lst[_])
print(ans)