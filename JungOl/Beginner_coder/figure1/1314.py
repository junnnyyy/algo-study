n = int(input())
lst = [0] * n ** 2
for i in range(n ** 2):
    lst[i] = chr((i % 26) + 65)

arr = [[0]*n for _ in range(n)]
for i in range(n):
    if i % 2:
        for j in range(n-1, -1, -1):
            arr[n-j-1][i] = lst[i*n+j]
    else:
        for j in range(n):
            arr[j][i] = lst[i*n+j]

for _ in range(n):
    print(*arr[_])
