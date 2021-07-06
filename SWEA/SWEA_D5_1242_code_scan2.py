import sys

sys.stdin = open('input.txt')
hexi = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

deci = {
    '3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4,
    '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9,
}

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    password = set()

    for n in range(N - 1, -1, -1):
        m = M - 1
        while m >= 0:
            if code[n][m] != '0':
                code[n] = str(bin(int(code[n][:m + 1], 16)))[2:]
                pw = code[n].rstrip('0')
                password.add(pw)
                break
            else:
                m -= 1
    password = list(password)

    # 굵기 찾고, 56의 배수로 패스워드 이진법 형태 만들기
    for i in range(1, len(password)):
        password[i] = password[i].replace(password[i - 1], '').rstrip('0')
    multiple = []
    for i in range(len(password)):
        temp = len(password[i]) // 56
        addition = 56 - (len(password[i]) % 56)
        if addition <= 3 * (temp + 1):
            temp += 1
            password[i] = '0' * addition + password[i]
            multiple.append(temp)
    if t == 13 :
        for i in range(len(password)):
            print(password[i])
        # print(t, len(password))
        # print('#', t, password[49])
        # print(len(multiple))
        # print(multiple[-1])

    # 비율 찾기
    portion = ['' for _ in range(len(multiple))]
    for i in range(len(multiple)):
        cnt = 0
        j = 0
        # if multiple[i] and len(password[i]):
        now = password[i][j]
        while j < len(password[i]):
            if now == password[i][j]:
                cnt += 1
            else:
                portion[i] += str(cnt//multiple[i])
                now = password[i][j]
                cnt = 1
            j += 1
        portion[i] += str(cnt // multiple[i])
    # print(portion)
    # print(len(portion[0]))

    # 십진법 해독
    password = []
    for i in range(len(portion)):
        temp = ''
        for j in range(0, len(portion[i]), 4):
            a = portion[i][j:j+4]
            temp += str(deci[a])
        password.append(temp)
    # 패스워드 검증
    ans = 0
    for k in range(len(password)):
        target = password[k]
        inspect = 0
        for i in range(len(target) - 1):
            now = int(target[i])
            inspect = inspect + now if i % 2 else inspect + 3 * now
        # 검증숫자 더해서
        inspect += int(target[-1])
        if not inspect % 10:
            for idx in range(len(target)):
                ans += int(target[idx])
    print('#{} {}'.format(t, ans))
