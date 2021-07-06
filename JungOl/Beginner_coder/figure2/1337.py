def go(r, c):
    r += 1
    c += 1

def up(r):
    r -= 1

def left(c):
    c -= 1

n = int(input())
arr = [[''] * n for _ in range(n)]
arr[0][0] = 0
a = 1
# 0,0 1,1 2,2 3,3 4,4 5,5 5,4 5,3 5,2 5,1 5,0
r, c = 1, 1
rr = n-1
cc = 0
while 0 <= r < n and 0 <= c < n:
    arr[r][c] = a % 10
    a += 1
    if r == n-1:
        left(c)
    elif c == 0:
        up(r)
    else:
        go(r, c)

