def magnetic(lst):
    S, cnt = [], 0
    while lst:
        top = lst.pop()
        if top == 1: # 1 이면 밖으로 나가려함. 2가 스택안에있으면 2랑 부딪
            if S:
                S.pop()
                cnt += 1
        elif top == 2:
            S.append(top)
    return cnt


for t in range(1, 2):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    retable = [[table[j][i] for j in range(N)] for i in range(N)]

    ans = 0
    for i in range(N):
        ans += magnetic(retable[i])
    print('#{} {}'.format(t, ans))
