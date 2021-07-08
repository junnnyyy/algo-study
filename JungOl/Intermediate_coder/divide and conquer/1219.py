def bin_s(gap):
    total, i = 0, 0
    while i < c:
        if paper[i]:
            total += 1
            i += gap
        else:
            i += 1
    return total


r, c = map(int, input().split())
cp = int(input())
N = int(input())
if cp == N:
    print(1)
else:
    paper = [0] * c
    m, M = 0, 0
    for n in range(N):
        x, y = map(int, input().split())
        if x > m: # 행 기준 맥시멈
            m = x
        paper[y-1] = 1
        if M <= y - 1: # 뒤쪽에 불필요한 부분 제거
            M = y
    b = (M // cp) + 1 if M % cp else M // cp # 열 기준 맥시멈
    if m >= b:
        print(m)
    else:
        ans = b
        start, end = m, b
        while start <= end: # 이진 탐색
            mid = (start + end) // 2
            total = bin_s(mid)
            if total <= cp:
                ans = mid
                end = mid - 1
            elif total > cp:
                start = mid + 1
        print(ans)

