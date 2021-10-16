def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    cnt = 0
    for num in lottos:
        if num != 0:
            if num in win_nums:
                cnt += 1
    bottom = ranking[cnt]
    top = ranking[cnt + zero]
    answer = [top, bottom]
    return answer