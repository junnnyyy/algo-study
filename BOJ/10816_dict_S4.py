import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))
cnt = dict()
ans = ''
for _ in range(n):
    if not cnt.get(cards[_]):
        cnt[cards[_]] = 1
    else:
        cnt[cards[_]] += 1
for __ in range(m):
    if not cnt.get(check[__]):
        ans += '0 '
    else:
        ans += str(cnt[check[__]]) + ' '
sys.stdout.write(ans)
