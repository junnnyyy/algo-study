def one(n, i):
    if i == n:
        print(*sel1)
        return
    for j in range(1, 7):
        sel1[i] = j
        one(n, i + 1)

def two(n, i, k):
    if i == n:
        print(*sel2)
        k += 1
        return
    for j in range(k, 7):
        sel2[i] = j
        two(n, i + 1, j)

def three(n, i):
    if i == n:
        print(*sel3)
        return
    for j in range(1, 7):
        if not checked[j]:
            sel3[i] = j
            checked[j] = 1
            three(n, i + 1)
            checked[j] = 0

N, M = map(int, input().split())
sel1 = [0] * N
sel2 = [0] * N
sel3 = [0] * N
if M == 1:
    one(N, 0)
elif M == 2:
    two(N, 0, 1)
elif M == 3:
    checked = [1] + [0] * 6
    three(N, 0)
