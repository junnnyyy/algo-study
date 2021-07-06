def search(r, c, num=''):
    if len(num) == 7:
        number.add(num)
        return

    num += str(grid[r][c])
    for idx in range(4):
        now_r, now_c = r + dr[idx], c + dc[idx]
        if 0 <= now_r < 4 and 0 <= now_c < 4:
            search(now_r, now_c, num)


for t in range(1, int(input()) + 1):
    grid = [list(map(int, input().split()))for _ in range(4)]

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    number = set()

    for i in range(4):
        for j in range(4):
            search(i, j)

    print('#{} {}'.format(t, len(number)))
