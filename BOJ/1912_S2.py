n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n # nums[i]부터 시작하는 숫자중 가장큰 합
dp[n-1] = nums[n-1]
for i in range(n-2, -1, -1):
    dp[i] = max(nums[i], dp[i+1] + nums[i])

print(max(dp))
