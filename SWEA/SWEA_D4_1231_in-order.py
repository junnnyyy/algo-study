def in_order(idx):
    # 왼쪽 자식 있으면
    global ans
    if idx > 0:
        # 왼쪽 자식 있으면
        in_order(left[idx])
        # 왼쪽 자식 없으면
        ans += chars[idx]
        # 오른쪽 자식 있으면
        in_order(right[idx])


for t in range(1, 11):
    N = int(input())
    chars, left, right = [0] * (N+1), [0] * (N+1), [0] * (N+1)
    ans = ''
    for n in range(N):
        in_lst = list(input().split())
        while len(in_lst) < 4:
            in_lst.append(0)
        node, ch = int(in_lst[0]), in_lst[1]
        chars[node], left[node], right[node] = ch, int(in_lst[2]), int(in_lst[3])
    in_order(1)
    print('#{} {}'.format(t, ans))

