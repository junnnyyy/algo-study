def comb(i, j, n, r):
    if i == r:
        # ar을 정하는 조합
        print(c)
        return
    for k in range(j, n - r + i + 1):
        c[i] = archers[k]
        comb(i + 1, k + 1, n, r)

# 좌 상 하 만
dr, dc = [0, -1, 1], [-1, 0, 0]
def simulation(lst, bg, enemy_cnt):
    ar1, ar2, ar3 = lst






N, M, D = map(int, input().split())
max_enemy = 0
battle_ground = [list(map(int, input().split())) for _ in range(N)]
bg = []
enemy_cnt = 0
for i in range(M):
    lst = []
    for j in range(N):
        if battle_ground[j][i]:
            enemy_cnt += 1
        lst.append(battle_ground[j][i])
    lst.append(-1)
    bg.append(lst)
ac = len(bg[0])

archers = list(range(M))
c = [0] * 3
comb(0, 0, M, 3)


for _ in range(M):
    print(bg[_])