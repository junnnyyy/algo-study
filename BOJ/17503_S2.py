import sys
sys.stdin = open('input.txt', 'r')


def achol_calc(lo, to):
    global ans
    while lo <= to:
        m = (lo + to) // 2
        n, total, idx = 0, 0, 0
        while n < N and idx < K:
            if beer[idx][1] <= m:
                total += beer[idx][0]
                n += 1
            idx += 1
        if total < M:
            lo = m + 1
        elif total >= M and n == N:
            if ans == -1 or m < ans:
                ans = m
            to = m - 1


N, M, K = map(int, input().split())
total_v = 0
beer = []
lowest, top = 2 ** 31, 0
for k in range(K):
    v, c = map(int, input().split()) # 선호도, 도수
    beer.append((v, c))
    if c < lowest:
        lowest = c
    if c > top:
        top = c
beer.sort(reverse=True)
ans = -1
achol_calc(lowest, top)
print(ans)


