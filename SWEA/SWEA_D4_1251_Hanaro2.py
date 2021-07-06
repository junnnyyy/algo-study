def findset(a):
    while a != root[a]:
        a = root[a]
    return a


def mst():
    total = 0
    cnt = 0
    for i in range(len(l)):
        a, b = l[i][1], l[i][2]
        if findset(a) != findset(b):
            total += l[i][0]
            root[findset(b)] = findset(a)
            cnt += 1
            if cnt == N-1:
                return total


for t in range(1, int(input()) + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    root = [i for i in range(N + 1)]
    l = []
    for i in range(N):
        for j in range(N):
            if i != j:
                dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
                l.append([dist, i, j])
    l.sort()
    total = mst()
    print(f'#{t} {round(total * e)}')
