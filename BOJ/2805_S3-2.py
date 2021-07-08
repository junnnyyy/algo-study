import sys


def bin_search(low, high):
    mid, total = 0, 0
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for idx in range(N):
            val = trees[idx] - mid
            if val > 0:
                total += val
        if total == M:
            return mid, total, True
        elif total > M: # 좀 덜 베어야 하는 경우
            low = mid + 1
        else: # 더 베어야 하는 경우
            high = mid - 1
    return mid, total, False


N, M = map(int, sys.stdin.readline().split()) # 나무가 N 그루
trees = list(map(int, sys.stdin.readline().split()))
low, high = 0, max(trees)
res, total, same = bin_search(low, high)
if not same:
    if total < M:
        res -= 1
print(res)

