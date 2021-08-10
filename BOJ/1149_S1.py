n = int(input())
coloring = list(list(map(int, input().split())) for _ in range(n))
compare = [[0] * 3 for _ in range(n)]
compare[0] = coloring[0][:]
for i in range(1, n):
    for j in range(3):
        # i번째 줄의 j번째 색을 고를때 최소
        compare[i][j] = min(compare[i-1][j-1], compare[i-1][j-2]) + coloring[i][j]
print(min(compare[-1]))
