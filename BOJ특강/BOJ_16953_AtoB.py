A, B = map(int, input().split())
cnt = 0
while B > A:
    if B % 10 == 1:
        B //= 10
        cnt += 1
    elif not B % 2:
        B /= 2
        cnt += 1
    else:
        break
if A == B:
    print(cnt+1)
else:
    print(-1)