def b(D):
    if D == 3:
        return 1
    else:
        return a(D-1) + b(D-1)


def a(D):
    if D == 3:
        return 1
    else:
        return b(D-1)


D, K = map(int, input().split())
aa = a(D)
bb = b(D)
ans_a = 0
ans_b = 0
for i in range(1, K//aa):
    B = (K - aa * i)/bb
    if i < B and B == int(B):
        ans_b = int(B)
        ans_a = i
        break

print(ans_a)
print(ans_b)
