N, K = map(int, input().split())
time = 0
while True:
    if N > 500000 or K > 500000:
        print(-1)
        break
    time += 1
    K += time
    if 2 * N <= K:
        N *= 2
    else:
        if K >= N:
            N += 1
        else:
            N -= 1

    print(N, K)
    if N == K:
        print(time)
        break

