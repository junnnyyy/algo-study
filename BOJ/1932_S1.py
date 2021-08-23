N = int(input())
tri = [[int(input()), 0]]
for n in range(1, N):
    tmp = list(map(int, input().split())) + [0]
    tri.append(tmp)
    for i in range(n+1):
        tri[n][i] = max(tri[n-1][i-1], tri[n-1][i]) + tri[n][i]
print(max(tri[-1]))





