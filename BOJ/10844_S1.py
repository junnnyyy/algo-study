n = int(input())
memo = [0] * max(n+1, 3)
memo[1] = 0
memo[2] = 1
memo[3] = 4
for i in range(4, n+1):
    memo[i] = (memo[i-1]-memo[i-2])*2 + memo[i-1]
print(memo)
res = 9 * (2**(n-1)) - memo[n]
print(res%(10**9))