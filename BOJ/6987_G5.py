# 승무패 합은 5
# 무승부한 나라의 수는 짝수이고 무승부 횟수도 짝수여야한다.
# 승의합과 패의 합이 같아야한다.
# 승의 합과 패의 합은 15 - 무승부횟수/2

for _ in range(4):
    ans = 1
    result = list(map(int, input().split()))
    if sum(result) == 30:
        win, draw, lose = [], [], []
        for i in range(0, 18, 3):
            w, d, l = result[i], result[i+1], result[i+2]
            if w + d + l == 5:
                win.append(w)
                draw.append(d)
                lose.append(l)
            else:
                ans = 0
                print(ans, end=' ')
                break
        if not ans:
            print(ans, end=' ')
            continue
        if sum(draw) % 2 or draw.count(0) % 2:
            ans = 0
            print(ans, end=' ')
            continue
        if sum(win) != sum(lose):
            ans = 0
            print(ans, end=' ')
            continue
        if sum(win) != 15 - sum(draw)//2 or sum(lose) != 15 - sum(draw)//2:
            ans = 0
            print(ans, end=' ')
            continue
        print(ans, end=' ')
    else:
        ans = 0