def calc(a, b, ans):
    if a == 0:
        ans += b
    elif a == 1:
        ans -= b
    elif a == 2:
        ans *= b
    else:
        ans = int(ans / b)
    return ans


def perm(n, pick, ans):
    global M, m
    if n == pick:
        if ans > M:
            M = ans
        elif ans < m:
            m = ans
        return
    for i in range(pick, n):
        operator[pick], operator[i] = operator[i], operator[pick]
        perm(n, pick + 1, calc(operator[pick], operand[pick + 1], ans))
        operator[pick], operator[i] = operator[i], operator[pick]


for t in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    operator = []
    for idx in range(4):
        for i in range(lst[idx]):
            operator.append(idx)
    operand = list(map(int, input().split()))
    M, m = -10 ** 8, 10 ** 8
    perm(N-1, 0, operand[0])
    print('#{} {}'.format(t, M-m))
