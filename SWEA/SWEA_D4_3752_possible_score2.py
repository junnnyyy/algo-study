for t in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))

    for i in range(1 << N):
        subset = []
        for j in range(i):
            if i & (1 << j):
                subset.append(score[j])
