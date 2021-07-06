ans = 0
for n in range(int(input())):
# n번 선수의 점수
    score = list(map(int, input()))
    order = [0] * 9
    order[3] = 0
# n번 타자의 현위치
    position = [0] * 9
    position[3] = score[order[3]] # 4





pass






# i번 선수의 현 위치 position[order[i]
for i in range(9):
    position[order[i]] = score[i]
    if score[i]:
        idx = order[i]
        while idx < 9:
            idx -= 1
            position[order[i]] += position[idx]

