n, m = map(int, input().split())

if m == 1:
    for i in range(1, n+1):
        for _ in range(n):
            print(i, end=' ')
        print()

elif m == 2:
    for j in range(n):
        if j  % 2 :
            for i in range(n, 0, -1):
                print(i, end=' ')
            print()
        else:
            for i in range(1, n+1):
                print(i, end=' ')
            print()

elif m == 3:
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            print(i*j, end=' ')
        print()