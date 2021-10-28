import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_min_max(x, y):
    global min_x, max_x, min_y, max_y
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

for _ in range(int(input())):
    nx, ny = 0, 0
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    idx = 0
    for val in input():
        idx %= 4
        if val == 'F':
            nx, ny = nx + d[idx][0], ny + d[idx][1]
            find_min_max(nx, ny)
        elif val == 'B':
            nx, ny = nx - d[idx][0], ny - d[idx][1]
            find_min_max(nx, ny)
        elif val == 'R':
            idx += 1
        else:
            idx -= 1
    ans = abs(max_x - min_x) * abs(max_y - min_y)
    print(ans)