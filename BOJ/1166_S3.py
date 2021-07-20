def bin_s(l, r):
    global A
    for _ in range(60): # 10^9/ 2^n <=  10 ^ -9, n = 60
        m = (l + r) / 2
        if (sq[0]//m) * (sq[1]//m) * (sq[2]//m) >= N:
            if A < m:
                A = m
            l = m
        else:
            r = m
    return


N, L, W, H = map(int, input().split())
sq = [L, W, H]
A = 10 ** (-9)
l = 10 ** (-9)
r = min(sq)
bin_s(l, r)
print(round(A, 9))







