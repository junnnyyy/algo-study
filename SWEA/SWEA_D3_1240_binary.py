nums = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9,
}

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    code = [input() for n in range(N)]
    password = []
    # 패스워드 위치 찾기 맨뒤는 항상 1임
    for n in range(N - 1, -1, -1):
        for m in range(M - 1, -1, -1):
            if code[n][m] == '1':
                password.append(code[n][m - 56 + 1:m + 1])
                break
            if m < 56:
                break
    # 패스워드 십진수 변환
    for i in range(len(password)):
        pw = ''
        for j in range(1, 9):
            c = password[i][7 * (j - 1):7 * j]
            pw += str(nums[c])
        password[i] = pw
    # 패스워드 검증
    inspect = 0
    for i in range(len(password[0]) - 1):
        now = int(password[0][i])
        inspect = inspect + now if i % 2 else inspect + 3 * now
    # 검증숫자 더해서
    inspect += int(password[0][-1])
    ans = 0
    if not inspect % 10:
        for idx in range(len(password[0])):
            ans += int(password[0][idx])
    print('#{} {}'.format(t, ans))
