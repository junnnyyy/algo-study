deci = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9,
}
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    code = list(set(code))
    ans = 0
    for i in range(len(code)):
        code[i] = bin(int(code[i], 16))[2:]
    password = ''
    lst = set()
    for i in range(len(code)):
        p1, p2, p3, p4 = 0, 0, 0, 0
        for j in range(len(code[i])):
            if p4 and code[i][j] == '0':
                multiple = min(p2, p3, p4)
                word = str(p2//multiple) + str(p3//multiple) + str(p4//multiple)
                p1, p2, p3, p4 = 0, 0, 0, 0
                password += str(deci[word])
            if len(password) == 8:
                inspect = int(password[7])
                for idx in range(7):
                    if not idx % 2:
                        inspect += int(password[idx]) * 3
                    else:
                        inspect += int(password[idx])
                if not inspect % 10 and password not in lst:
                    lst.add(password)
                    for k in password:
                        ans += int(k)
                password = ''

            if not p2 and code[i][j] == '0':
                p1 += 1
            elif not p3 and code[i][j] == '1':
                p2 += 1
            elif p2 and code[i][j] == '0':
                p3 += 1
            elif p3 and code[i][j] == '1':
                p4 += 1

    print('#{} {}'.format(t, ans))
