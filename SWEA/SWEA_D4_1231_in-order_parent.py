def in_order(idx):
    global ans
    # 왼쪽 자식 있으면
    if 0 < 2*idx <= N:
        in_order(2*idx)
    # 왼쪽 자식 없으면
    ans += chars[idx]
    # 오른쪽 자식 있으면
    if 0 < 2*idx+1 <= N:
        in_order(2*idx+1)


for t in range(1, 11):
    N = int(input())
    chars = [0] * (N+1)
    ans = ''
    for n in range(N):
        lst = list(input().split())
        chars[int(lst[0])] = lst[1]

    in_order(1)
    print('#{} {}'.format(t, ans))

