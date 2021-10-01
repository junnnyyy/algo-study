P = int(input())
for p in range(1, P+1):
    lst = list(map(int, input().split()))
    lst = lst[1:]
    ordered_lst = []
    ans = 0
    for i in range(len(lst)):
        if i == 0 or max(ordered_lst) < lst[i]:
            # 앞에 나보다 작은애가 없으면 그냥 그대로 세운다.
            ordered_lst.append(lst[i])
        else:
            # 아니면 나보다 큰애중 제일 앞에 있는애 찾는다.
            for j in range(20):
                if ordered_lst[j] > lst[i]:
                    ordered_lst.insert(j, lst[i])
                    ans += (i-j)
                    break
    print(p, ans)




