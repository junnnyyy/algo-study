import sys


N = int(input())
A = list(map(int, sys.stdin.readline().split()))
s = []
op = [-1] * N

for i in range(N):
    if not s or A[i] > s[-1][0]:
        while s and s[-1][0] < A[i]:
            val, idx = s.pop()
            op[idx] = A[i]
    s.append((A[i], i))
print(*op)
