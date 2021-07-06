def find_max(brick):
    max_col = 0
    for i in range(W):
        col = 0
        for j in range(H):
            col += brick[i][j]
        if col > max_col:
            max_col = col
    return max_col


for t in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    can_break = brick[:]
    total = 0
    for i in range(H):
        for j in range(W):
            val = can_break[i][j]
            if val != 1 and val:
                cnt = 0
                total += 1
                l, r = max(0, j - val + 1), min(W, j + val)
                for k in range(l, r):
                    if brick[i][k]:
                        cnt += 1
                can_break[i][j] = cnt
    pang = 0
    for _ in range(H):
        print(can_break[_])

for n in range(N):
    pass