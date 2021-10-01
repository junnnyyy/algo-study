DIR = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}

def next_dir(now_dir, watch):
    if now_dir == 'E':
        next = 'S' if watch else 'N'
    elif now_dir == 'N':
        next = 'E' if watch else 'W'
    elif now_dir == 'W':
        next = 'N' if watch else 'S'
    else:
        next = 'W' if watch else 'E'
    return next

M, n = map(int, input().split())
x, y = 0, 0
now_dir = 'E'
for i in range(n):
    comm, num = input().split()
    num = int(num)
    if comm == 'MOVE':
        x += DIR.get(now_dir)[0] * num
        y += DIR.get(now_dir)[1] * num
    elif comm == 'TURN':
        now_dir = next_dir(now_dir, num)
    if 0 > x or M <= x or 0 > y or M <= y:
        break
if 0 > x or M <= x or 0 > y or M <= y:
    print(-1)
else:
    print(x, y)










