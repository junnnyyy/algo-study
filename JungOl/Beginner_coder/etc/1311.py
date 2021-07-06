def straight():
    for i in range(6):
        if hands[i] and hands[i+1] and hands[i+2] and hands[i+3] and hands[i+4]:
            return i
    return False

R = [0] * 10
B = [0] * 10
Y = [0] * 10
G = [0] * 10
hands = [0] * 10
ans = 0
for i in range(5):
    color, num = input().split()
    num = int(num)
    hands[num] += 1
    if color == 'R':
        R[num] = 1
    elif color == 'B':
        B[num] = 1
    elif color == 'Y':
        Y[num] = 1
    elif color == 'G':
        G[num] = 1

# 스트레이트플러쉬 가장 높은 숫자+ 900
if sum(R) == 5 or sum(B)==5 or sum(Y) == 5 or sum(G) == 5:
    for i in range(6):
        if straight():
            ans = straight() + 900 + 4
            break
# 플러시 가장 높은 숫자 + 600
    else:
        max_num = 0
        for _  in range(9, -1, -1):
            if hands[_]:
                max_num = _
                break
        ans = 600 + max_num

# 4장의 숫자가 같을 때 같은 숫자+800 포카드
elif 4 in hands:
    four = hands.index(4)
    ans = 800 + four
# 풀하우스 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700
elif 3 in hands:
    tri = hands.index(3)
    if 2 in hands:
        pair = hands.index(2)
        ans = tri * 10 + pair + 700
# 트리플 + 400
    else:
        ans = tri + 400

# 스트레이트 가장 높은 숫자+ 500
elif straight():
    ans = 500 + 4 + straight()

# 투페어 큰거 * 10 + 작은거 + 300
elif hands.count(2) == 2:
    small = 0
    big = 0
    for i in range(10):
        if hands[i] == 2:
            if not small:
                small = i
            else:
                big = i
                break
    ans = big * 10 + small + 300
# 원페어 같은거 + 200
elif hands.count(2) == 1:
    pair = hands.index(2)
    ans = 200 + pair
# 하이카드+ 100
else:
    card = 0
    for i in range(9, -1, -1):
        if hands[i]:
            card = i
            break
    ans = 100 + card

print(ans)





