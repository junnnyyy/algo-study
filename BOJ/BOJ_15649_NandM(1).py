import sys


def powerset(idx, cnt):
    if idx >= N:
        if sel.count(1) == cnt:
            for i in range(N):
                if sel[i] == 1:
                    print(nums[i], end=' ')
            print()
        return
    sel[idx] = 1
    powerset(idx+1, cnt)
    sel[idx] = 0
    powerset(idx+1, cnt)


N, M = map(int, sys.stdin.readline().split())
nums = range(1, N+1)
sel = [0] * N
powerset(0, M)