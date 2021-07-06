def calc(a, b, ans):
    if a == '+':
        ans += b
    elif a == '-':
        ans -= b
    elif a == '/':
        ans = int(ans / b)
    else:
        ans *= b
    return ans


#  calc(operator[pick], operand[pick + 1], ans)
def permutation(perm, visited):
    global M, m
    if len(perm) == N-1:
        ans = operand[0]
        for idx in range(N-1):
            ans = calc(perm[idx], operand[idx + 1], ans)
        if ans > M:
            M = ans
        if ans < m:
            m = ans
    else:
        for i in range(N-1):
            if not visited[i] and (i == 0 or operator[i-1] != operator[i] or visited[i-1]):
                perm.append(operator[i])
                visited[i] = 1
                permutation(perm, visited)
                visited[i] = 0
                perm.pop()


def create():
    visited = [0] * (N-1)
    permutation([], visited)


for t in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    operator = ['+'] * lst[0] + ['-'] * lst[1] + ['*'] * lst[2] + ['/'] * lst[3]
    operand = list(map(int, input().split()))
    M, m = -10 ** 8, 10 ** 8
    create()
    print('#{} {}'.format(t, M-m))
