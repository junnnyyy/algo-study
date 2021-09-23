n, m = map(int, input().split())
s, e = 0, 1
print(s, e)
s = 1
cnt = 1
while cnt < m:
    e += 1
    cnt += 1
    print(s, e)
s = e-1
while e < n - 1:
    s += 1
    e += 1
    print(s, e)


