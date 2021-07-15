def cutting(a, t):
    if t == 0:
        return min(l)
    min_piece = min(l)
    min_idx = l.index(min_piece)
    if min_idx == 0:
        l[min_idx] = min_piece + l[min_idx+1]
        l.pop(min_idx+1)
    elif min_idx == len(l) - 1:
        l[min_idx] = min_piece + l[min_idx-1]
        l.pop(min_idx-1)
    else:
        if l[min_idx - 1] < l[min_idx+1]:
            tmp = l[min_idx-1]
            idx = min_idx - 1
        else:
            tmp = l[min_idx+1]
            idx = min_idx + 1
        l[min_idx] = min_piece + tmp
        l.pop(idx)
    return cutting(a, t-1)


N, M, L = map(int, input().split())
s, q, ans = [0] * M, [0] * N, [0] * N
l = [0] * (M + 1)
for m in range(M):
    s[m] = int(input())
    if m == 0:
        l[m] = s[m]
    else:
        l[m] = s[m] - s[m-1]
l[M] = L - s[M-1]

for n in range(N):
    q[n] = int(input())
for n in range(N-1, -1, -1):
    if n < N-1:
        ans[n] = cutting((q[n+1]-q[n]), (q[n+1]-q[n]))
    else:
        ans[n] = cutting(M-q[n], M-q[n])
for n in range(N):
    print(ans[n])
