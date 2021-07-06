n = int(input())
arr = [[0] * n for _ in range(n)]
dr = [1, -1, 0,1]
dc = [0, 1, 1, -1]
# 0이 안돼면 2, 2가 안돼면 0
a, r, c = 1, 0, 0
arr[r][c] = a
while a < n*n:
    for i in range(4):
        if i == 0:
            r, c = r + dr[i], c + dc[i]
            if r >= n:
                r -= 1
                c += 1
            a += 1
            arr[r][c] = a
        elif i == 1:
            while 0 < r and c < n-1:
                r, c = r + dr[i], c + dc[i]
                a += 1
                arr[r][c] = a
        elif i == 2:
            r, c = r + dr[i], c + dc[i]
            if c >= n:
                r += 1
                c -= 1
            a += 1
            arr[r][c] = a
        else:
            while 0 < c and r < n-1:
                r, c = r + dr[i], c + dc[i]
                a += 1
                arr[r][c] = a

for _ in range(n):
    print(*arr[_])