T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    mom, son = 1, 1
    for i in range(m, m-n, -1):
        mom *= i
    for i in range(1, n+1):
        son *= i
    res = mom // son
    print(res)
