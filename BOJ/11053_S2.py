N = int(input())
A = list(map(int, input().split()))
incl = [0] * N # 자기 자신을 포함하는 가장 긴 수열의 길이

# 나보다 A, i 작은 중 제일 큰 incl
for i in range(N):
    tmp = 0
    if i == 0 or min(A) == A[i]:
        incl[i] = 1
    else:
        for idx in range(i):
            if A[i] > A[idx] and incl[idx] > tmp:
                tmp = incl[idx]
        incl[i] = tmp + 1
print(max(incl))

