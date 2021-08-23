n = int(input())
wine = [0] * n
dp = [0] * n
for _ in range(n):
    wine[_] = int(input())

if n >= 1:
    dp[0] = wine[0]
if n >= 2:
    dp[1] = dp[0] + wine[1]
if n >= 3:
    dp[2] = max(wine[1] + wine[2], dp[0] + wine[2], dp[1])
for i in range(3, n):
    # 내가 합의 두번째, 내가 합의 첫번째, 내가 안포함
    dp[i] = max(wine[i] + wine[i-1] + dp[i-3], dp[i-2] + wine[i], dp[i-1])
print(max(dp))




