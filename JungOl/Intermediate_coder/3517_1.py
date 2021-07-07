import sys


def bin_search(start, end, b):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] > b:
            end = mid - 1
        elif A[mid] < b:
            start = mid + 1
        else:
            return mid
    return -1

N = int(input())
A = list(map(int, sys.stdin.readline().split()))  # 오름차순 정렬되어있음
Q = int(input())
B = list(map(int, sys.stdin.readline().split()))


ans = [0] * Q
start, end = 0, N - 1
for i in range(Q):
    res = bin_search(start, end, B[i])
    if res != -1:
        ans[i] = res
    else:
        ans[i] = -1
print(*ans)


