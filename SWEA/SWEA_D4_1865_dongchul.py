def distrib(n, pick, poss):
    global max_poss
    if poss <= max_poss:
        return
    if pick == n:
        if max_poss < poss:
            max_poss = poss
            return

    for i in range(pick, n):
        task[pick], task[i] = task[i], task[pick]
        distrib(n, pick+1, poss*(P[pick][task[pick]]/100))
        task[pick], task[i] = task[i], task[pick]


for t in range(1, int(input())+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    task = list(range(0, N))
    max_poss = 0
    distrib(N, 0, 1)
    print('#{} {:0.6f}'.format(t, max_poss*100))
