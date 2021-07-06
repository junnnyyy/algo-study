s, e = map(int, input().split())
while not (s in range(2, 10) and e in range(2, 10)):
    print("INPUT ERROR!")
    s, e = map(int, input().split())

if s > e:
    for j in range(1, 10):
        for i in range(s, e - 1, -1):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}   ', end='')
            else:
                print(f'{i} * {j} = {i * j}   ', end='')
        print()

else:
    for j in range(1, 10):
        for i in range(s, e + 1):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}   ', end='')
            else:
                print(f'{i} * {j} = {i * j}   ', end='')
        print()