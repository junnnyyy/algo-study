n = int(input()) # 높이 n과 종류 m

if n in range(1, 101) and n % 2:
    a = n // 2 + 1
    for i in range(1, a):
        print((i - 1) * ' ' + '*' * (2 * i - 1))
    for i in range(a, 0, -1):
        print((i - 1) * ' ' + '*' * (2 * i - 1))
else:
    print('INPUT ERROR!')