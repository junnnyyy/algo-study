def prim(s):
    MST, l = [0] * N, [M] * N
    l[s] = 0
    for i in range(N):
        min_i, min_val = 0, M
        for j in range(N):
            # mst가 아닌것중 가장 작은 값 찾기
            if not MST[j] and min_val > l[j]:
                min_val = l[j]
                min_i = j
        # 최소가중치가 설정된 MST
        MST[min_i] = 1
        l[min_i] = min_val
        for k in range(N):
            if not MST[k] and l[k] > w[min_i][k]:
                l[k] = w[min_i][k]
    return sum(l)


for t in range(1, int(input()) + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    M = 2*(10**12)
    w = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                w[i][j] = (x[i]-x[j]) ** 2 + (y[i]-y[j]) ** 2
                w[j][i] = (x[i]-x[j]) ** 2 + (y[i]-y[j]) ** 2
    total = prim(0)
    print(f'#{t} {round(total * e)}')
