def bin_search(s, e):
    global l, r
    min_val = abs(liq[s] + liq[e])
    while s < e:
        val = liq[s] + liq[e]
        if val == 0:
            l, r = s, e
            return
        else:
            if abs(val) < min_val: #0 에서 더 가까우면 범위를 더 줄여가보고
                min_val = abs(val)
                l, r = s, e
            if val < 0:
                s += 1
            else:
                e -= 1
    return


N = int(input())
liq = list(map(int, input().split()))
liq.sort()
mid = abs(liq[0] + liq[-1])
l, r = 0, N-1
bin_search(l, r)
print(liq[l], liq[r])
