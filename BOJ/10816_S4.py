cnt = [0] * 20000002
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
ans = [0] * m
for _ in range(n):
    cnt[cards[_]+10000001] += 1
for __ in range(m):
    ans[__] = cnt[check[__]+10000001]

print(*ans)
