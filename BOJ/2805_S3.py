import sys
from collections import Counter


def bin_search(low, high):
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for height, cnt in trees:
            if height > mid:
                total += (height - mid) * cnt
        if total == M:
            return mid
        elif total < M:
            high = mid - 1
        elif total > M:
            low = mid + 1
    return high


N, M = map(int, sys.stdin.readline().split()) # 나무가 N 그루
trees = Counter(list(map(int, sys.stdin.readline().split()))).most_common()
l, h = 0, max(trees)[0]
print(bin_search(l, h))


