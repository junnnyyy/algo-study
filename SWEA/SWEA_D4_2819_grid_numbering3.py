N, K = map(int, input().split())
lst = list(map(int, input().split()))
print(lst)
idx = K - 1
ans = 1
while idx < N:
    idx += K
    ans += 1
print(ans)
