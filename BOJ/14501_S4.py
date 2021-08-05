N = int(input())
sch = [list(map(int, input().split())) for _ in range(N)]
max_lst = [0] * N
for n in range(N):
    payday = sch[n][0] + n - 1
    rev = sch[n][1]
    yesterday = max_lst[n-1] # 어제까지의 최댓값
    for i in range(payday, N):
        max_lst[i] = max(max_lst[i], yesterday + rev)
print(max(max_lst))
