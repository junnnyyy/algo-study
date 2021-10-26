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
    nkr, nkc = kr + dr, kc + dc
    if 0 <= nkr < 8 and 0 <= nkc < 8:
        if nkr == sr and nkc == sc:
            nsr = sr + dr
            nsc = sc + dc
            if 0 <= nsr < 8 and 0 <= nsc < 8:
                kr, kc = nkr, nkc
                sr, sc = nsr, nsc
            else:
                continue
        else:
            kr, kc = nkr, nkc
    else:
        continue

king = chr(kc+65) + str(kr+1)
stone = chr(sc+65) + str(sr+1)
print(king)
print(stone)