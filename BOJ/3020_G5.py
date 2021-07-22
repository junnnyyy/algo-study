# 석순의 높이 >= 날아가는 구간: 부숨
# 종유석높이 > H - 날아가는 구간: 부숨
# 석순 구간:  \/
# 종유석 구간: /\

N, H = map(int, input().split())
seok, jong = [0]*H, [0]*H
for n in range(N):
    if not n % 2:
        seok[int(input())-1] += 1
    else:
        jong[-int(input())] += 1
for h in range(H-2, -1, -1):
    seok[h] = seok[h] + seok[h+1]
for h in range(1, H):
    jong[h] = jong[h-1] + jong[h]
cnt = [seok[h] + jong[h] for h in range(H)]
print(min(cnt), cnt.count(min(cnt)))
