def chain(idx, T, ex):
    print(idx, a[idx], ex)
    if ex == N or idx <= 0 or idx >= N-1:
        return ex
    if T < 0:
        if a[idx] + T <= a[idx-1]:
            print('left')
            return chain(idx-1, T+1, ex+1)
    elif T > 0:
        if a[idx] + T >= a[idx + 1]:
            print('right')
            return chain(idx+1, T+1, ex+1)
    return ex


def bin_s():
    global explode
    for i in range(N):
        m = a[i]
        print(m)
        right, left = 0, 0
        if i <= N-2:
            right = chain(m, 1, 1)
        if i >= 1:
            left = chain(m, -1, 1)
        total = right + left
        if total > explode:
            explode = total
    return

N = int(input())
a = []
explode = 0
for _ in range(N):
    idx = int(input())
    a.append(idx)
a.sort()
bin_s()
print(explode)




