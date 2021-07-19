def bin_search(l, r):
    global ans
    while l <= r:
        gap = (l + r) // 2
        cnt, start = 1, X[0]
        for x in X:
            if x - start >= gap:
                start = x
                cnt += 1
        if cnt >= C:
            ans = gap
            l = gap + 1
        else:
            r = gap - 1
    return


N, C = map(int, input().split())
X = [int(input()) for _ in range(N)]
ans = 1
X.sort()
r = X[-1] - X[0]
bin_search(1, r)
print(ans)