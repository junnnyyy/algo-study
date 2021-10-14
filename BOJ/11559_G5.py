# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 터트릴 뿌요 정해주기
def bfs(r, c, color):
    global is_bomb
    q = [(r, c)]
    # 터질 뿌요의 후보군을 담을 리스트
    candi = []
    # 캔디체크 해준 자리인지 확인 해줄 리스트
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
        # 뿌요가 4개넘게 모여서 터트렸음을 체크
        is_bomb = True
        # print(candi)
        for i in range(len(candi)):
            xr, xc = candi[i]
            lst[xr][xc] = 0


# 뿌요 터트리기
def rm_zero(lst):
    for i in range(6):
        y = len(lst[i])
        for j in range(y - 1, -1, -1):
            if lst[i][j] == 0:
                lst[i].pop(j)
    return


# 인덱스 에러 방지를 위한 '.'을 채워주는 함수
def padding(lst):
    for i in range(6):
        y = len(lst[i])
        val = 12 - y
        lst[i] += ['.'] * val


lst = [[0] * 12 for _ in range(6)]
for i in range(12):
    tmp = list(input())
    for j in range(len(tmp)):
        lst[j][11 - i] = tmp[j]

ans = 0
# 현재 반복에서 터진적 있는지 체크하기 위한 boolean 값
is_bomb = True
while True:
    checked = [[0] * 12 for _ in range(6)]
    is_bomb = False
    for i in range(6):
        tmp_ans = 0
        y = len(lst[i])
        for j in range(y):
            if lst[i][j] != '.':
                # print(i, j, lst[i][j])
                bfs(i, j, lst[i][j])
    rm_zero(lst)
    padding(lst)
    # 터졌으면 또 터질지 해보기
    if is_bomb:
        ans += 1
    else:
        break
    # for _ in range(6):
    #    print(lst[_])
print(ans)