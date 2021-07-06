for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans = 'ON' if ((1 << N)-1) & M == ((1 << N)-1) else 'OFF'
    print('#{} {}'.format(t, ans))