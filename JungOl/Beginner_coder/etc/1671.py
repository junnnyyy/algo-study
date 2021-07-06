n = int(input())
arr = [[0] * 102 for _ in range(102)]
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x+1, x+11):
        for j in range(y+1, y+11):
            arr[i][j] = 1

for i in range(102):
    for j in range(102):
        if arr[i][j]:
            if arr[i-1][j] + arr[i][j-1] + arr[i+1][j] + arr[i][j+1] == 3:
                ans += 1
            elif arr[i-1][j] + arr[i][j-1] + arr[i+1][j] + arr[i][j+1] == 2:
                ans += 2
print(ans)