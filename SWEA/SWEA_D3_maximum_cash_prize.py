for t in range(1, int(input()) + 1):
    nums, chg = map(int, input().split())
    result = [int(char) for char in str(nums)]
    N = len(result)
    org_chg = chg
    for i in range(N - 2):
        max_num = max(result[i:])
        for j in range(N - 1, i - 1, -1):
            if result[j] == max_num:
                max_idx = j
                break
        if i != max_idx:
            result[i], result[max_idx] = result[max_idx], result[i]
            chg -= 1
            if chg == 0: break

    # 맥스넘이 여러개면 뒤에 두개는 교환을 해도 되고 안해도됨
    if org_chg > 1 and result.count(max(result)) > 1:
        if result[-1] > result[-2]:
            result[-1], result[-2] = result[-2], result[-1]
    elif chg % 2 == 1 and result.count(max(result)) == 1:
        result[-1], result[-2] = result[-2], result[-1]

    str_res = [str(_) for _ in result]
    str_res = int(''.join(str_res))

    print('#{} {}'.format(t, str_res))
