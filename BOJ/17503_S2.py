N, M, K = map(int, input().split())
beer = []
for k in range(K):
    v, c = map(int, input().split()) # 선호도, 도수
    beer.append((v, c))
liver = 0


