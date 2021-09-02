def fac(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def comb(n, k):
    return fac(n)//(fac(k) * fac(n-k))

N, K = map(int, input().split())
ans = (comb(N+K-1, N))% 1000000000
print(ans)
