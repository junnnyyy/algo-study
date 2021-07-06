def findset(a):
    if a == root[a]:
        return a
    return findset(root[a])


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    root = list(range(N + 1))

    for _ in range(M):
        a, b = map(int, input().split())
        root[findset(b)] = findset(a)
    for i in range(N+1):
        root[i] = findset(i)
    root = set(root[1:])
    print('#{} {}'.format(t, len(root)))
