# def dijkstra(s):
#     U = [0] * N
#     U[s] = 1
#     D = list(L[s])
#     min_val = 1000001 ** 2
#     min_i = 99
#     while sum(U) != N:
#         for i in range(N):
#             if not U[i] and U[i] < min_val:
#                 min_val = U[i]
#                 min_i = i
#         U[min_i] = 1
#         for j in range(N):
#             D[j] = min(D[j], D[min_i] + L[i][j])
#     return sum(D)
def findset(a):
    while a != root[a]:
        a = root[a]
    return a


def mst():
    total = 0
    for i in range(len(l)):
        a, b = l[i][1], l[i][2]
        if findset(a) != findset(b):
            total += l[i][0]
            root[findset(b)] = findset(a)
    return total


for t in range(1, int(input()) + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    root = [i for i in range(N + 1)]
    # l [dist, start, destination]
    l = []
    for i in range(N):
        for j in range(N):
            if i != j:
                dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
                l.append([dist, i, j])
    l.sort()
    total = mst()
    print(f'#{t} {round(total * e)}')
