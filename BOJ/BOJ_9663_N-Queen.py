# # 유망한지 체크하는 함수
# def check(x, y, lst):
#     for i in range(len(lst)):
#         if lst[i][1] == y or abs(lst[i][0] - x) == abs(lst[i][1] - y):
#             return False
#     return True


# 퀸 놔보기
def nQueen(x, y, queen):
    global ans
    queen.append((x, y))
    if len(queen) == N:
        ans += 1
    x += 1
    for i in range(N):
        for j in range(len(queen)):
            if queen[j][1] == i or abs(queen[j][0] - x) == abs(queen[j][1] - i):
                break
        else:
            nQueen(x, i, queen)
            queen.pop()


N = int(input())
ans = 0
for i in range(N):
    queen = []
    nQueen(0, i, queen)
print(ans)