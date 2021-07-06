m = int(input())
n = int(input())

lst = [False, False] + [True] * (n-1)
prime = []
min_p = n
sum_p = 0
for i in range(2, n+1):
    if lst[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            lst[j] = False
for k in range(m, n+1):
    if lst[k]:
        if k < min_p: min_p = k
        sum_p += k
if sum_p:
    print(sum_p)
    print(min_p)
else:
    print(-1)