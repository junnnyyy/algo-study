N = int(input())
length = 2 * N - 1
arr = [[' '] * length for _ in range(length)]
dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

char = 0
r, c = 0, N - 1
arr[r][c] = chr(65 + (char % 26))
for n in range(N-1, 0, -1):
    for i in range(4):
        for j in range(n):
            char += 1
            r, c = r + dr[i], c + dc[i]
            if j == n - 1 and i == 3:
                r, c = r - dr[i], c - dc[i] -1
            arr[r][c] = chr(65 + (char % 26))

for _ in range(length):
    print(*arr[_])


