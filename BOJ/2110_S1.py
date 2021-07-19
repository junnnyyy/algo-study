def bin_search(l, r):
    ans = 0
    while l <= r:
        gap = (l + r) // 2
        cnt, start = 0, s
        for x in X:
            if x - start >= gap: # 기준간격보다 멀면
                start = x
                cnt += 1 # 공유기 설치
        if cnt >= c: # 더 넓게 설치할 수 있겠다 싶으면.
            ans = gap
            l = gap + 1
        else:
            r = gap -1
    return ans


N, C = map(int, input().split())
X, s = [], 0
s = 0
for _ in range(N):
    if not _:
        s = int(input())
    else:
        X.append(int(input()))
r, c, l = X[-1], C - 1, s # l은 이진 탐색을 위함, s는 시작 기준점을 위함
X.sort()
print(bin_search(l, r))
