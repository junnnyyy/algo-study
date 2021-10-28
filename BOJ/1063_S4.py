direction = {
    'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
    'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB':(-1, -1)
}

king, stone, n = input().split()
kr, kc = int(king[1]) - 1, ord(king[0]) - 65
sr, sc = int(stone[1]) - 1, ord(stone[0]) - 65
n = int(n)
for _ in range(n):
    dr, dc = direction.get(input())
    # 왕이 이동할 위치
    nkr, nkc = kr + dr, kc + dc
    # 왕이 이동할 곳이 판 위에 있다면
    if 0 <= nkr < 8 and 0 <= nkc < 8:
        # 돌이랑 만난다면 돌을 밀어..
        if nkr == sr and nkc == sc:
            nsr = sr + dr
            nsc = sc + dc
            # 밀린돌이 판위에 있다면
            if 0 <= nsr < 8 and 0 <= nsc < 8:
                kr, kc = nkr, nkc
                sr, sc = nsr, nsc
            else:
                continue
        # 돌이랑 안만나면 왕만 움직이기
        else:
            kr, kc = nkr, nkc
    else:
        continue

# chr써서 다시 위치 체계 바꿔주기
king = chr(kc+65) + str(kr+1)
stone = chr(sc+65) + str(sr+1)
print(king)
print(stone)