ans, low_ans = '', '' # 초기값
n = int(input())
while n:
    lst, low_lst = [], []
    for _ in range(n):
        tmp = input()
        low_tmp = tmp.lower()
        lst.append(tmp)
        low_lst.append((low_tmp, _))
    low_lst.sort()
    print(lst[low_lst[0][1]])
    n = int(input())

