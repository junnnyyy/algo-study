s, e = map(int, input().split())

if s > e:
    for i in range(s, e - 1, -1):
        for j in range(1, 10):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}   ', end='')
            else:
                print(f'{i} * {j} = {i * j}   ', end='')
            if not j % 3:
                print()
        print()
else:
    for i in range(s, e + 1):
        for j in range(1, 10):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}   ', end='')
            else:
                print(f'{i} * {j} = {i * j}   ', end='')
            if not j % 3:
                print()
        print()