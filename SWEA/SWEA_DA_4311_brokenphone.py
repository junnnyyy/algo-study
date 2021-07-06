import sys
sys.stdin = open('input.txt', 'r')
# 터치 가능한 숫자들의 개수 N
# 터치 가능한 연산자들의 개수 O
# 최대 터치 가능한 횟수 M
# 원하는 숫자 W

def making(W, touch):
    global max_touch
    if W in numbers:
        touch += 1
    if max_touch > touch:
        max_touch = touch
    return
    W = str(W)
    if touch > max_touch:
        return
    a, b = int(W[0]), int(W[-1])

    if a in numbers:
        touch += 1
        W = W[1:]
        return making(W, touch)
    elif b in numbers:
        touch += 1
        W = W[:-1]
        return making(W, touch)
    else:
        W = int(W)
        for i in numbers:
            if not i:
                continue
            touch += 1
            if i < W and 1 in opers: # +
                touch += 1 # i를 누름
                making(W-i, touch)
                touch -= 2
            elif i < W and 3 in opers:
                if not W % i:  # *
                    touch += 1
                    making(W // i, touch)
                    touch -= 2
            elif i > W and 2 in opers:  # -
                touch += 1
                making(W + i, touch)
                touch -= 2
            elif i > W and 4 in opers:  # //
                touch += 1
                making(W - i, touch)
                touch -= 2
        return



for t in range(1, int(input())+1):
    N, O, M = map(int, input().split())
    numbers = list(map(int, input().split())) # 눌리는 숫자들
    opers = list(map(int, input().split())) # 눌리는 연산자들 1~4 + - * /
    W = int(input())
    max_touch = M
    if min(numbers) > W and 2 not in opers and 4 not in opers or\
            max(numbers) < W and 1 not in opers and 3 not in opers:
        print(f'#{t} -1')
    else:
        making(W, 0)
        if max_touch == M:
            print(f'#{t} -1')
        else:
            print(f'#{t} {max_touch}')