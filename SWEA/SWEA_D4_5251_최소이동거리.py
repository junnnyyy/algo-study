import sys
sys.stdin = open('input2.txt', 'r')


def dijkstra(s):
    # s에서 각 지점별 최소 거리
    l = list(adj[s])
    dijk = {s}
    l[s] = 0
    while len(dijk) != N+1:
        min_i, min_val = -1, M
        for j in range(N+1):
            # 최소거리가 확정 안된 것들 중 가장 작은 거리
            if j not in dijk and min_val > l[j]:
                min_val = l[j]
                min_i = j
        dijk.add(min_i)
        for k in range(N+1):
            l[k] = min(l[k], l[min_i] + adj[min_i][k])
    return l[N]


for t in range(1, int(input())+1):
    N, E = map(int, input().split())
    M = 10 ** 7
    adj = [[M] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        # 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w
        s, e, w = map(int, input().split())
        adj[s][e] = w
    ans = dijkstra(0)
    print(f'#{t} {ans}')






