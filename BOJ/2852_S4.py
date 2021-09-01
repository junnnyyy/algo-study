goal = ['00:00']
n = int(input())
one, two = [0], [0]

for _ in range(n):
    team, time = input().split()
    goal.append(time)
    if team == '1':
        one.append(one[-1]+1)
        two.append(two[-1])
    else:
        two.append(two[-1] + 1)
        one.append(one[-1])

goal.append('48:00')
ans1_m, ans1_s, ans2_m, ans2_s = 0, 0, 0, 0

for i in range(n, 0, -1):
    minute = int(goal[i+1][:2]) - 1
    second = int(goal[i+1][3:]) + 60
    if one[i] > two[i]:
        ans1_m += minute - (int(goal[i][:2]))
        ans1_s += second - (int(goal[i][3:]))
    elif one[i] < two[i]:
        ans2_m += minute - (int(goal[i][:2]))
        ans2_s += second - (int(goal[i][3:]))

ans1_m += ans1_s // 60
ans1_s = ans1_s % 60
ans2_m += ans2_s // 60
ans2_s = ans2_s % 60

print(f'{str(ans1_m).zfill(2)}:{str(ans1_s).zfill(2)}')
print(f'{str(ans2_m).zfill(2)}:{str(ans2_s).zfill(2)}')