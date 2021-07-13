import sys
sys.stdin = open('input.txt', 'r')


def achol_calc(lo, to):
    global ans
    while lo <= to:
        m = (lo + to) // 2
        n, total = 0, 0
        for idx in range(K):
            if n == N or K - idx < N - n:
                break
            if beer[idx][1] <= m:
                total += beer[idx][0]
                n += 1
        if total >= M and n == N:
            ans = m
            to = m - 1
        else:
            lo = m + 1


N, M, K = map(int, input().split())
total_v = 0
beer = []
lowest = 2147483647 # 최저 도수
top = 0 # 최고 도수
for k in range(K):
    v, c = map(int, input().split()) # 선호도, 도수
    beer.append((v, c))
    if c < lowest:
        lowest = c
    if c > top:
        top = c

beer.sort(reverse=True) # 선호도가 높은것 순으로 정렬
summ = 0
for _ in range(N):
    summ += beer[_][0]
if summ < M:
    print(-1)
else:
    ans = top
    achol_calc(lowest, top)
    print(ans)


