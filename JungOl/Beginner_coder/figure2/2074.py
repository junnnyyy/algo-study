n = int(input())
arr = [[0] * n for _ in range(n)]

a, r, c = 1, 0, n // 2

while a < n * n:
    arr[r][c] = a
    if not a % n:
        r += 1
    else:
        r -= 1
        c -= 1
    if r < 0:
        r = n - 1
    elif r > n - 1:
        r = 0
    if c < 0:
        c = n - 1
    a += 1
arr[n-1][n//2] = n * n
for _ in range(n):
    print(*arr[_])
