n = int(input())
lst = [0] * n ** 2
for i in range(n ** 2):
    lst[i] = chr((i % 26) + 65)

arr = [[' '] * n for _ in range(n)]
k = 0
for i in range(n):
    for j in range(n - i):
        arr[(j + i) % n][n - 1 - j % n] = lst[k]
        k += 1

for _ in range(n):
    for __ in range(n):
        print(arr[_][__], end=' ')
    print()
