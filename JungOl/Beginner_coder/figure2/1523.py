n, m = map(int, input().split()) # 높이 n과 종류 m

if n in range(1, 101) and m in range(1, 4):
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n, 0, -1):
            print('*' * i)
    else:
        for i in range(1, n+1):
            print((n - i) * ' ' + '*' * (2 * i - 1))
else:
    print('INPUT ERROR!')