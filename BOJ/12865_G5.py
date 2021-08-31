N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for n in range(N)]
for n in range(N):
    wei,val = map(int, input().split())
    if n == 0:
        for i in range(wei, K+1):
            dp[n][i] = val
    else:
        for i in range(1, K+1):
            # 무게가 i일 때 최대 가치
            if i >= wei:
                dp[n][i] = max(dp[n-1][i], dp[n-1][i-wei]+val)
            else:
                dp[n][i] = dp[n-1][i]
print(max(dp[N-1]))
