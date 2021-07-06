dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
n = int(input())
arr = [[0] * n for _ in range(n)]

r, c, num = 0, 0, 1
arr[r][c] = num
for j in range(n-1, 0, -2):
    for i in range(4):
        for k in range(j):
            r, c = r + dr[i], c + dc[i]
            num += 1
            if num == n**2+1:
                break
            if i == 3 and k == j-1:
                r, c = r - dr[i], c - dc[i] + 1
            arr[r][c] = num


for _ in range(n):
    print(*arr[_])