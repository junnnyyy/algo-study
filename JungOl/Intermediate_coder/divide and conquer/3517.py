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
for i in range(Q):
    B[i] = [B[i], i]

ans = [0] * Q
start, end = 0, N - 1

sort_b = sorted(B)

for i in range(Q // 2):
    b = sort_b[i]
    res = bin_search(start, end, b[0])
    if res != -1:
        start = res + 1
        ans[b[1]] = res
    else:
        ans[b[1]] = -1

    b = sort_b[Q - 1 - i]
    res = bin_search(start, end, b[0])
    if res != -1:
        end = res - 1
        ans[b[1]] = res
    else:
        ans[b[1]] = -1

if Q % 2:
    b = sort_b[Q // 2]
    res = bin_search(start, end, b[0])
    if res != -1:
        start = res + 1
        ans[b[1]] = res
    else:
        ans[b[1]] = -1

print(*ans)


