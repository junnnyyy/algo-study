def comb(i, j, n, r):
    # i 는 c의 인덱스 고를자리
    # j는 사용가능한 S리스트 인덱스들의 시작
    if i == r:
        print(*c)
    else:
        for k in range(j, n-r+i+1): # n개중 r개를 선택
            c[i] = S[k]
            comb(i+1, k+1, n, r)


while True:
    S = list(map(int, input().split()))
    if len(S) == 1:
        break
    h, S = S[0], S[1:]
    c = [0] * 6
    comb(0, 0, h, 6)
    print()