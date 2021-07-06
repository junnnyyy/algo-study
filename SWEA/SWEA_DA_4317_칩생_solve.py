import sys


sys.stdin = open("input2.txt", 'r')

def is_chip(r, c):
    if 0 <= r < H-1 and 0 <= c < W-1 and not wf[r][c] and not wf[r][c + 1] and not wf[r + 1][c] and not wf[r + 1][c + 1]:
        return True
    return False


def counting(r, c, cnt, wf):
    global max_chip
    if is_chip(r, c):
        wf[r][c], wf[r][c + 1], wf[r + 1][c], wf[r + 1][c + 1] = 2, 2, 2, 2
        cnt += 1
        if c + 2 < W - 1:
            counting(r, c + 2, cnt, wf)
            wf[r][c], wf[r][c + 1], wf[r + 1][c], wf[r + 1][c + 1] = 0, 0, 0, 0
            return
        elif r + 1 < H - 1:
            counting(r + 1, 0, cnt, wf)
            wf[r][c], wf[r][c + 1], wf[r + 1][c], wf[r + 1][c + 1] = 0, 0, 0, 0
            return
        else:
            if cnt > max_chip:
                max_chip = cnt
            return

    else:
        if 0 <= c + 1 < W - 1:
            counting(r, c + 1, cnt, wf)
            return
        elif 0 <= r + 1 < H - 1:
            counting(r + 1, 0, cnt, wf)
            return
        else:
            if cnt > max_chip:
                max_chip = cnt
            # print('*',cnt)
            return


for t in range(1, int(input())+1):
    H, W = map(int, input().split())
    wf = [list(map(int, input().split())) for _ in range(H)]
    max_chip = 0
    # need_check = []
    # checked_r = [0] * H
    # checked_c = [0] * W
    for r in range(H-1):
        for c in range(W-1):
            if not wf[r][c]:
                # print(f'[{r},{c}]', end=' ')
                counting(r, c, 0, wf)
                # # 확인할 가치가 있다면,
                # if r >= 2 and is_chip(r, c) and not checked_r[r-2]:
                #     print(f'[{r},{c}]', checked_r)
                #     checked_r[r], checked_c[c] = 1, 1
                #     need_check.append((r, c))
                # elif c >= 2 and is_chip(r, c) and not checked_c[c-2]:
                #     checked_r[r], checked_c[c] = 1, 1
                #     need_check.append((r, c))
                # elif (0 <= r < 2 or 0 <= c < 2) and is_chip(r, c):
                #     checked_r[r], checked_c[c] = 1, 1
                #     print(checked_r)
                #     need_check.append((r, c))
    # if t == 1:
    #     print(need_check)
    #
    # while need_check:
    #     r, c = need_check.pop()
    #     print(f'[{r},{c}]')
    #     counting(r, c, 0, wf)

    print(max_chip)
