def calc(operator):
    if operator == '*':
        tree[i] = tree[info[i][2]] * tree[info[i][3]]
    elif operator == '+':
        tree[i] = tree[info[i][2]] + tree[info[i][3]]
    elif operator == '-':
        tree[i] = tree[info[i][2]] - tree[info[i][3]]
    elif operator == '/':
        tree[i] = tree[info[i][2]] / tree[info[i][3]]


for t in range(1, 11):
    N = int(input())
    info = [list() for _ in range(N + 1)]
    tree = [0] * (N + 1)

    for n in range(1, N + 1):
        info[n] = list(input().split())
        info[n][0] = int(info[n][0])
        info[n][-1] = int(info[n][-1])
        info[n][-2] = int(info[n][-2])
        tree[info[n][0]] = info[n][1]

    for i in range(N, 0, -1):
        if not isinstance(tree[i], int):
            calc(tree[i])
    print('#{} {}'.format(t, int(tree[1])))
