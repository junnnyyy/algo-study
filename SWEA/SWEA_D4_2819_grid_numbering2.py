def coupon(n, N, M):
    if n == 12:
        prize = N // 12
        return prize

    special = N // n
    normal = M // (12 - n)
    prize = min(special, normal)

    a = N - n*prize
    b = M - (12-n)*prize

    if prize == normal and a + b // 12 != 0:
        prize += (special - n * prize + normal) // 12

    return prize


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    result = 0

    if N < 5:
        print(result)

    else:
        for i in range(5, 13, 1):
            ans = coupon(i, N, M)
            if ans > result:
                result = ans
        print(result)


