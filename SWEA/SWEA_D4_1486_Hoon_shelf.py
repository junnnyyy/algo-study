def subset(idx):
    global ans
    tower = 0
    if not ans:
        return
    if idx == N:
        for i in range(len(sel)):
            if sel[i] == 1:
                tower += hgt[i]
        if 0 <= tower - M < ans:
            ans = tower - M

        return

    sel[idx] = 1
    subset(idx+1)

    sel[idx] = 0
    subset(idx+1)


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    hgt = list(map(int, input().split()))
    ans = sum(hgt) - M
    sel = [0] * N

    subset(0)
    print('#{} {}'.format(t, ans))
