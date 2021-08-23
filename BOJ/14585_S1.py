N, M = map(int, input().split()) # N개의 사탕 바구니 각M개씩 들어있음
candies = []
for n in range(N):
    where = list(map(int, input().split()))
    candies.append(where)
print(candies)
time = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)] # i, j i번째 좌표를 j번째로 갔을때 최대사탕

for i in range(N):
    dp[0][i] = 15 - (candies[i][0] + candies[i][1])

for i in range(1, N):
    tmp = 0
    for j in range(N):
        if j != i and dp[i-1][j] > tmp:
            tmp = dp[i-1][j]
        dp[i][j] = max(dp[i+1:i-1])

print(dp)