# def powerset(idx):
#     if idx == N:
#         total = [score[n] * sel[n] for n in range(N)]
#         if sum(total) not in psb_score:
#             psb_score.append(sum(total))
#             return
#     else:
#         sel[idx] = 0
#         powerset(idx+1)
#
#         sel[idx] = 1
#         powerset(idx+1)


for t in range(1, int(input())+1):
    N = int(input())
    ans = N
    score = list(map(int, input().split()))
    set_score = set(score)
    ans -= len(score)-len(set_score)
    sel = [0] * N
    psb_score = []


    print('#{} {}'.format(t, len(psb_score)))
