def cutting(r, c, l):
    global white, blue
    total = 0
    for i in range(r, r+l):
        total += sum(pp[i][c:c+l])
    if total == 0:
        white += 1
        return
    elif total == l ** 2:
        blue += 1
        return
    else:
        cutting(r, c, l//2)
        cutting(r+l//2, c, l//2)
        cutting(r, c+l//2, l//2)
        cutting(r+l//2, c+l//2, l//2)


white, blue = 0, 0
N = int(input())
pp = [list(map(int, input().split())) for _ in range(N)]
cutting(0, 0, N)
print(white)
print(blue)