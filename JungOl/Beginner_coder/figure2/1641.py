n, m = map(int, input().split())

if m in range(1, 4) and n in range(1, 101) and n % 2 :
    if m == 1:
        a = 1
        for i in range(1, n+1):
            b = ''
            if i % 2 :
                for _ in range(i):
                    b += str(a) + ' '
                    a += 1
                print(b)
            else:
                for _ in range(i):
                    b = str(a) + ' ' + b
                    a += 1
                print(b)

    elif m == 2:
        for i in range(n, 0, -1):
            print('  ' * (n - i) + (str(n - i) + ' ') * (2 * i - 1))
    else:
        a = list(range(1, n//2+2))
        for i in range(n//2):
            print(*a[:i+1])
        for i in range(n//2, -1, -1):
            print(*a[:i+1])
else:
    print('INPUT ERROR!')