import sys
sys.stdin = open("input.txt", 'r')
# 1
# 15 7

# 세로
def win1(r, c, color):
    if r <= 15:
        if r == 0 or (r > 0 and board[r-1][c] != color):
            for i in range(4):
                if board[r+i][c] != color:
                    return False
            if r + 5 == 20 or (r + 5 < 20 and board[r+5][c] != color):
                return True


# 가로
def win2(r, c, color):
    if c <= 15:
        if c == 0 or (c > 0 and board[r][c-1] != color):
            for i in range(4):
                if board[r][c+i] != color:
                    return False
            if c + 5 == 20 or (c + 5 < 20 and board[r][c+5] != color):
                return True


# 대각선 왼쪽 아래
def win3(r, c, color):
    if r <= 15 and c >= 4:
        if r == 0 or c == 19 or (board[r-1][c+1] != color):
            for i in range(4):
                if board[r+i][c-i] != color:
                    return False
            if r + 5 == 20 or c-5 == 0 or (board[r+5][c-5] != color):
                return True


# 대각선 오른쪽 아래
def win4(r, c, color):
    if r <= 15 and c <= 15:
        if r == 0 or c == 0 or (board[r-1][c-1] != color):
            for i in range(4):
                if board[r+i][c+i] != color:
                    return False
            if r + 5 == 20 or c + 5 == 20 or (board[r+5][c+5] != color):
                return True


board = [list(map(int, input().split())) for _ in range(19)]
winner = 0
r, c = 0, 0
for i in range(19):
    if winner:
        break
    for j in range(19):
        if board[i][j]:
            a = board[i][j]
            if board[i+1][j] == a:
                res = win1(i, j, a)
                if res:
                    winner = a
                    r, c = i, j
                    break
            if board[i][j+1] == a:
                res = win2(i, j, a)
                if res:
                    winner = a
                    r, c = i, j
                    break
            if board[i+1][j-1] == a:
                res = win3(i, j, a)
                if res:
                    winner = a
                    r, c = i, j
                    break
            if board[i+1][j+1] == a:
                res = win4(i, j, a)
                if res:
                    winner = a
                    r, c = i, j
                    break

print(winner)
print(r+1, c+1)


