def bin_search(s, e):
    while s <= e:
        m = (s + e) // 2


N, C = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))
X.sort()
print(X)
