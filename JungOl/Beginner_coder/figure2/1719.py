n, m = map(int, input().split()) # 높이 n과 종류 m

if n in range(1, 101) and m in range(1, 5) and n % 2:
    a = n // 2 + 1
    if m == 1:
        for i in range(1, a+1):
            print('*' * i)
        for i in range(a-1, 0, -1):
            print('*' * i)
    elif m == 2:
        for i in range(1, a+1):
            print((a - i) * ' ' + '*' * i)
        for i in range(a-1, 0, -1):
            print((a - i) * ' ' + '*' * i)
    elif m == 3:
        for i in range(a, 1, -1):
            print((a - i) * ' ' + '*' * (2 * i - 1))
        for i in range(1, a + 1):
            print((a - i) * ' ' + '*' * (2 * i - 1))
    else:
        for i in range(a, 0, -1):
            print((a - i) * ' ' + '*' * i)
        for i in range(2, a+1):
            print((a - 1) * ' ' + '*' * i)
else:
    print('INPUT ERROR!')