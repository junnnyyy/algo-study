for t in range(1, int(input())+1):
    D, N = map(int, input().split())
    T = 0
    for n in range(N):
        k, s = map(int, input().split())
        if T < (D-k) / s:
            T = (D-k) / s
    print('#{} {}'.format(t, D / T))